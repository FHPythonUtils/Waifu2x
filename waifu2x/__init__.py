from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

import numpy as np
from chainer.backends import cuda
from chainer.serializers.npz import load_npz
from PIL import Image

from . import iproc, reconstruct, srcnn, utils

THISDIR = str(Path(__file__).resolve().parent)


def denoise_image(args: argparse.Namespace, src: Image.Image, model) -> Image.Image:
	dst, alpha = split_alpha(src, model)
	print(f"Level {args.noise_level} denoising...", end=" ", flush=True)
	if args.tta:
		dst = reconstruct.image_tta(dst, model, args.tta_level, args.block_size, args.batch_size)
	else:
		dst = reconstruct.image(dst, model, args.block_size, args.batch_size)
	if model.inner_scale != 1:
		dst = dst.resize((src.size[0], src.size[1]), Image.LANCZOS)
	print("OK")
	if alpha is not None:
		dst.putalpha(alpha)
	return dst


def upscale_image(
	args: argparse.Namespace, src: Image.Image, scale_model, alpha_model=None
) -> Image.Image:
	dst, alpha = split_alpha(src, scale_model)
	for i in range(int(np.ceil(np.log2(args.scale_ratio)))):
		print("2.0x scaling...", end=" ", flush=True)
		model = scale_model if i == 0 or alpha_model is None else alpha_model
		if model.inner_scale == 1:
			dst = iproc.nn_scaling(dst, 2)  # Nearest neighbor 2x scaling
			alpha = iproc.nn_scaling(alpha, 2)  # Nearest neighbor 2x scaling
		if args.tta:
			dst = reconstruct.image_tta(
				dst, model, args.tta_level, args.block_size, args.batch_size
			)
		else:
			dst = reconstruct.image(dst, model, args.block_size, args.batch_size)
		if alpha_model is None:
			alpha = reconstruct.image(alpha, scale_model, args.block_size, args.batch_size)
		else:
			alpha = reconstruct.image(alpha, alpha_model, args.block_size, args.batch_size)
		print("OK")
	dst_w = int(np.round(src.size[0] * args.scale_ratio))
	dst_h = int(np.round(src.size[1] * args.scale_ratio))
	if dst_w != dst.size[0] or dst_h != dst.size[1]:
		print("Resizing...", end=" ", flush=True)
		dst = dst.resize((dst_w, dst_h), Image.LANCZOS)
		print("OK")
	if alpha is not None:
		if alpha.size[0] != dst_w or alpha.size[1] != dst_h:
			alpha = alpha.resize((dst_w, dst_h), Image.LANCZOS)
		dst.putalpha(alpha)
	return dst


def split_alpha(src: Image.Image, model) -> tuple[Image.Image, Image.Image | None]:
	alpha = None
	if src.mode in ("L", "RGB", "P"):
		srcRGBA = src.convert("RGBA")
		alphas = [x[1][-1] for x in srcRGBA.getcolors(src.size[0] * src.size[1])]
		if any(x < 255 for x in alphas):
			print(f"Alpha channel detected in image with mode={src.mode}")
			alpha = srcRGBA.split()[-1]
	rgb = src.convert("RGB")
	if src.mode in ("LA", "RGBA"):
		print("Splitting alpha channel...", end=" ", flush=True)
		alpha = src.split()[-1]
		rgb = iproc.alpha_make_border(rgb, alpha, model)
		print("OK")
	return rgb, alpha


def load_models(args: argparse.Namespace):
	ch = 3 if args.color == "rgb" else 1
	if args.model_dir is None:
		model_dir = THISDIR + f"/models/{args.arch.lower()}"
	else:
		model_dir = args.model_dir

	models = {}
	flag = False
	if args.method == "noise_scale":
		model_name = f"anime_style_noise{args.noise_level}_scale_{args.color}.npz"
		model_path = os.path.join(model_dir, model_name)
		if os.path.exists(model_path):
			models["noise_scale"] = srcnn.archs[args.arch](ch)
			load_npz(model_path, models["noise_scale"])
			alpha_model_name = f"anime_style_scale_{args.color}.npz"
			alpha_model_path = os.path.join(model_dir, alpha_model_name)
			models["alpha"] = srcnn.archs[args.arch](ch)
			load_npz(alpha_model_path, models["alpha"])
		else:
			flag = True
	if args.method == "scale" or flag:
		model_name = f"anime_style_scale_{args.color}.npz"
		model_path = os.path.join(model_dir, model_name)
		models["scale"] = srcnn.archs[args.arch](ch)
		load_npz(model_path, models["scale"])
	if args.method == "noise" or flag:
		model_name = f"anime_style_noise{args.noise_level}_{args.color}.npz"
		model_path = os.path.join(model_dir, model_name)
		if not os.path.exists(model_path):
			model_name = f"anime_style_noise{args.noise_level}_scale_{args.color}.npz"
			model_path = os.path.join(model_dir, model_name)
		models["noise"] = srcnn.archs[args.arch](ch)
		load_npz(model_path, models["noise"])

	if args.gpu >= 0:
		cuda.check_cuda_available()
		cuda.get_device(args.gpu).use()
		for _, model in models.items():
			model.to_gpu()
	return models


def main():
	# fmt:off
	p = argparse.ArgumentParser(description="Chainer implementation of waifu2x")
	p.add_argument("--gpu", "-g", type=int, default=-1)
	p.add_argument("--input", "-i", default="images/small.png")
	p.add_argument("--output", "-o", default="./")
	p.add_argument("--quality", "-q", type=int, default=None)
	p.add_argument("--model_dir", "-d", default=None)
	p.add_argument("--scale_ratio", "-s", type=float, default=2.0)
	p.add_argument("--tta", "-t", action="store_true")
	p.add_argument("--batch_size", "-b", type=int, default=16)
	p.add_argument("--block_size", "-l", type=int, default=128)
	p.add_argument("--extension", "-e", default="png", choices=["png", "webp"])
	p.add_argument("--arch", "-a", default="VGG7", choices=["VGG7", "0", "UpConv7", "1", "ResNet10", "2", "UpResNet10", "3"])
	p.add_argument("--method", "-m", default="scale", choices=["noise", "scale", "noise_scale"])
	p.add_argument("--noise_level", "-n", type=int, default=1, choices=[0, 1, 2, 3])
	p.add_argument("--color", "-c", default="rgb", choices=["y", "rgb"])
	p.add_argument("--tta_level", "-T", type=int, default=8, choices=[2, 4, 8])
	g = p.add_mutually_exclusive_group()
	g.add_argument("--width", "-W", type=int, default=0)
	g.add_argument("--height", "-H", type=int, default=0)
	g.add_argument("--shorter_side", "-S", type=int, default=0)
	g.add_argument("--longer_side", "-L", type=int, default=0)
	# fmt:on

	args = p.parse_args()
	if args.arch in srcnn.table:
		args.arch = srcnn.table[args.arch]

	models = load_models(args)

	input_exts = [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"]
	output_exts = [".png", ".webp"]
	outext = "." + args.extension

	outname = None
	outdir = args.output
	if os.path.isdir(args.input):
		filelist = utils.load_filelist(args.input)
	else:
		tmpname, tmpext = os.path.splitext(os.path.basename(args.output))
		if tmpext in output_exts:
			outext = tmpext
			outname = tmpname
			outdir = os.path.dirname(args.output)
			outdir = "./" if outdir == "" else outdir
		elif tmpext != "":
			raise ValueError(f"Format {tmpext} is not supported")
		filelist = [args.input]

	if not os.path.exists(outdir):
		os.makedirs(outdir)

	for path in filelist:
		if not Path(path).exists():
			p.print_help()
			sys.exit(1)
		tmpname, tmpext = os.path.splitext(os.path.basename(path))
		if outname is None or len(filelist) > 1:
			outname = tmpname
		outpath = os.path.join(outdir, f"{outname}{outext}")
		if tmpext.lower() in input_exts:
			src = Image.open(path)
			w, h = src.size[:2]
			if args.width != 0:
				args.scale_ratio = args.width / w
			elif args.height != 0:
				args.scale_ratio = args.height / h
			elif args.shorter_side != 0:
				if w < h:
					args.scale_ratio = args.shorter_side / w
				else:
					args.scale_ratio = args.shorter_side / h
			elif args.longer_side != 0:
				if w > h:
					args.scale_ratio = args.longer_side / w
				else:
					args.scale_ratio = args.longer_side / h

			dst = src.copy()
			start = time.time()
			outname += f"_(tta{args.tta_level})" if args.tta else "_"
			if "noise_scale" in models:
				outname += f"(noise{args.noise_level}_scale{args.scale_ratio:.1f}x)"
				dst = upscale_image(args, dst, models["noise_scale"], models["alpha"])
			else:
				if "noise" in models:
					outname += f"(noise{args.noise_level})"
					dst = denoise_image(args, dst, models["noise"])
				if "scale" in models:
					outname += f"(scale{args.scale_ratio:.1f}x)"
					dst = upscale_image(args, dst, models["scale"])
			print(f"Elapsed time: {time.time() - start:.6f} sec")

			outname += f"({args.arch}_{args.color}){outext}"
			if os.path.exists(outpath):
				outpath = os.path.join(outdir, outname)

			lossless = args.quality is None
			quality = 100 if lossless else args.quality
			icc_profile = src.info.get("icc_profile")
			icc_profile = "" if icc_profile is None else icc_profile
			dst.convert(src.mode).save(
				outpath, quality=quality, lossless=lossless, icc_profile=icc_profile
			)
			print(f"Saved as '{outpath}'")


if __name__ == "__main__":
	main()