from __future__ import annotations

import argparse
import random

import numpy as np
from PIL import Image

from . import data_augmentation, iproc


def _noise(src, p: np.ndarray, level: int):
	# YUV 444
	sampling_factor = "1x1,1x1,1x1"
	if np.random.uniform() < p:
		# YUV 420
		sampling_factor = "2x2,1x1,1x1"
	if level == 0:
		dst = iproc.jpeg(src, sampling_factor, random.randint(85, 100))
		return dst
	if level == 1:
		dst = iproc.jpeg(src, sampling_factor, random.randint(65, 90))
		return dst
	if level in (2, 3):
		# for level 3, --nr_rate 1
		rand = np.random.uniform()
		if rand < 0.6:
			dst = iproc.jpeg(src, sampling_factor, random.randint(25, 70))
		elif rand < 0.9:
			dst = iproc.jpeg(src, sampling_factor, random.randint(35, 70))
			dst = iproc.jpeg(dst, sampling_factor, random.randint(25, 65))
		else:
			dst = iproc.jpeg(src, sampling_factor, random.randint(50, 70))
			dst = iproc.jpeg(dst, sampling_factor, random.randint(35, 65))
			dst = iproc.jpeg(dst, sampling_factor, random.randint(25, 55))
		return dst
	raise ValueError(f"Unknown noise level: {level}")


def noise(src: np.ndarray, p: np.ndarray, p_chroma, level: int):
	if np.random.uniform() < p:
		with iproc.array_to_wand(src) as tmp:
			tmp = _noise(tmp, p_chroma, level)
			dst = iproc.wand_to_array(tmp)
		return dst
	return src


def scale(src: np.ndarray, filters, bmin, bmax, scale_):
	h, w = src.shape[:2]
	blur = np.random.uniform(bmin, bmax)
	rand = random.randint(0, len(filters) - 1)
	with iproc.array_to_wand(src) as tmp:
		tmp.resize(w // 2, h // 2, filters[rand], blur)
		if scale_:
			tmp.resize(w, h, "box")
		dst = iproc.wand_to_array(tmp)
	return dst


def noise_scale(
	src: np.ndarray, filters, bmin: float, bmax: float, scale_, p: np.ndarray, p_chroma, level: int
):
	h, w = src.shape[:2]
	blur = np.random.uniform(bmin, bmax)
	rand = random.randint(0, len(filters) - 1)
	with iproc.array_to_wand(src) as tmp:
		tmp.resize(w // 2, h // 2, filters[rand], blur)
		if np.random.uniform() < p:
			tmp = _noise(tmp, p_chroma, level)
		if scale_:
			tmp.resize(w, h, "box")
		dst = iproc.wand_to_array(tmp)
	return dst


def crop_if_large(src: np.ndarray, max_size: int):
	if max_size > 0 and src.shape[1] > max_size and src.shape[0] > max_size:
		point_x = random.randint(0, src.shape[1] - max_size)
		point_y = random.randint(0, src.shape[0] - max_size)
		dst = src[point_y : point_y + max_size, point_x : point_x + max_size, :]
		return dst
	return src


def preprocess(src: np.ndarray, args: argparse.Namespace):
	dst = data_augmentation.half(src, args.random_half_rate)
	dst = crop_if_large(dst, args.max_size)
	dst = data_augmentation.flip(dst)
	dst = data_augmentation.color_noise(dst, args.random_color_noise_rate)
	dst = data_augmentation.unsharp_mask(dst, args.random_unsharp_mask_rate)
	dst = data_augmentation.shift_1px(dst)
	return dst


def active_cropping(x, y, ly, size: int, scale_: int, p, tries: int):
	if size % scale_ != 0:
		raise ValueError("crop_size % scale must be 0")
	if x.shape[0] * scale_ != y.shape[0] or x.shape[1] * scale_ != y.shape[1]:
		raise ValueError(f"Scaled shape must be equal ({x.shape[:1]}, {y.shape[:1]})")

	size_x = size // scale_
	if np.random.uniform() < p:
		best_mse = 0
		for _ in range(tries):
			pw = random.randint(0, x.shape[1] - size_x) * scale_
			ph = random.randint(0, x.shape[0] - size_x) * scale_
			crop_x = x[
				ph // scale_ : ph // scale_ + size_x, pw // scale_ : pw // scale_ + size_x, :
			]
			crop_ly = ly[
				ph // scale_ : ph // scale_ + size_x, pw // scale_ : pw // scale_ + size_x, :
			]
			mse = np.mean(np.square(crop_ly - crop_x))
			if mse >= best_mse:
				best_mse = mse
				best_cx = crop_x
				best_cy = y[ph : ph + size, pw : pw + size, :]
		return best_cx, best_cy

	pw = random.randint(0, x.shape[1] - size_x) * scale_
	ph = random.randint(0, x.shape[0] - size_x) * scale_
	crop_x = x[ph // scale_ : ph // scale_ + size_x, pw // scale_ : pw // scale_ + size_x, :]
	crop_y = y[ph : ph + size, pw : pw + size, :]
	return crop_x, crop_y


def pairwise_transform(src: np.ndarray, args: argparse.Namespace):
	unstable_region_offset_x = 8
	unstable_region_offset_y = unstable_region_offset_x * args.inner_scale
	top = args.offset
	bottom = args.crop_size - top
	y = preprocess(src, args)

	if args.method == "scale":
		x = scale(
			y,
			args.downsampling_filters,
			args.resize_blur_min,
			args.resize_blur_max,
			args.inner_scale == 1,
		)
	elif args.method == "noise":
		if args.inner_scale != 1:
			raise ValueError("inner_scale must be 1")
		x = noise(y, args.nr_rate, args.chroma_subsampling_rate, args.noise_level)
	elif args.method == "noise_scale":
		if args.inner_scale == 1:
			raise ValueError("inner_scale must be > 1")
		x = noise_scale(
			y,
			args.downsampling_filters,
			args.resize_blur_min,
			args.resize_blur_max,
			False,
			args.nr_rate,
			args.chroma_subsampling_rate,
			args.noise_level,
		)

	y = y[
		unstable_region_offset_y : y.shape[0] - unstable_region_offset_y,
		unstable_region_offset_y : y.shape[1] - unstable_region_offset_y,
	]
	x = x[
		unstable_region_offset_x : x.shape[0] - unstable_region_offset_x,
		unstable_region_offset_x : x.shape[1] - unstable_region_offset_x,
	]
	lowres_y = y.copy()
	if args.crop_size != args.in_size:
		lowres_y = iproc.nn_scaling(y, 1 / args.inner_scale)

	patch_x = np.zeros((args.patches, args.ch, args.in_size, args.in_size), dtype=np.uint8)
	patch_y = np.zeros((args.patches, args.ch, args.out_size, args.out_size), dtype=np.uint8)

	for i in range(args.patches):
		crop_x, crop_y = active_cropping(
			x,
			y,
			lowres_y,
			args.crop_size,
			args.inner_scale,
			args.active_cropping_rate,
			args.active_cropping_tries,
		)
		if args.ch == 1:
			ycbcr_x = Image.fromarray(crop_x).convert("YCbCr")
			ycbcr_y = Image.fromarray(crop_y).convert("YCbCr")
			crop_x = np.array(ycbcr_x)[:, :, 0]
			crop_y = np.array(ycbcr_y)[top:bottom, top:bottom, 0]
			patch_x[i] = crop_x[np.newaxis, :, :]
			patch_y[i] = crop_y[np.newaxis, :, :]
		elif args.ch == 3:
			crop_y = crop_y[top:bottom, top:bottom, :]
			patch_x[i] = crop_x.transpose(2, 0, 1)
			patch_y[i] = crop_y.transpose(2, 0, 1)
	return patch_x, patch_y
