from __future__ import annotations

import random

import numpy as np
from PIL import Image, ImageFilter

from . import iproc


def unsharp_mask(src: np.ndarray, p) -> np.ndarray:
	if np.random.uniform() < p:
		tmp = Image.fromarray(src)
		percent = random.randint(10, 90)
		threshold = random.randint(0, 5)
		mask = ImageFilter.UnsharpMask(percent=percent, threshold=threshold)
		dst = np.array(tmp.filter(mask), dtype=np.uint8)
		return dst
	return src


def color_noise(src: np.ndarray, p, factor: float = 0.1) -> np.ndarray:
	if np.random.uniform() < p:
		tmp = np.array(src, dtype=np.float32) / 255.0
		scale = np.random.normal(0, factor, 3)
		ce, cv = iproc.pcacov(tmp)
		noise = cv.dot(ce.T * scale)[np.newaxis, np.newaxis, :]
		dst = np.clip(tmp + noise, 0, 1) * 255
		return dst.astype(np.uint8)
	return src


def flip(src: np.ndarray) -> np.ndarray:
	rand = random.randint(0, 3)
	dst = src
	if rand == 0:
		dst = src[::-1, :, :]
	elif rand == 1:
		dst = src[:, ::-1, :]
	elif rand == 2:
		dst = src[::-1, ::-1, :]
	return dst


def half(src: np.ndarray, p: np.ndarray) -> np.ndarray:
	if np.random.uniform() < p:
		filters = ("box", "box", "blackman", "cubic", "lanczos")
		rand = random.randint(0, len(filters) - 1)
		dst = iproc.scale(src, 0.5, filters[rand])
		return dst
	return src


def shift_1px(src: np.ndarray) -> np.ndarray:
	rand = random.randint(0, 3)
	x_shift = 0
	y_shift = 0
	if rand == 0:
		x_shift = 1
		y_shift = 0
	elif rand == 1:
		x_shift = 0
		y_shift = 1
	elif rand == 2:
		x_shift = 1
		y_shift = 1
	w = src.shape[1] - x_shift
	h = src.shape[0] - y_shift
	w = w - (w % 4)
	h = h - (h % 4)
	dst = src[y_shift : y_shift + h, x_shift : x_shift + w, :]
	return dst
