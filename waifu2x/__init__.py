"""Waifu2x is an image upscaling and noise reduction algorithm that gained
popularity for its ability to enhance the quality of anime-style images. The
implementation in Chainer, a deep learning framework, uses neural networks
to perform the image enhancement tasks.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import numpy as np
from chainer.backends import cuda
from chainer.link import Chain
from chainer.serializers.npz import load_npz
from PIL import Image

from waifu2x import iproc, reconstruct, srcnn, utils

THISDIR = Path(__file__).resolve().parent

# ruff: noqa: T201


def main() -> None:
	"""Run the program, from the main entry point."""
	run()


def denoise_image(
	args: argparse.Namespace,
	src: Image.Image,
	model: Chain,
	*,
	should_print: bool = True,
) -> Image.Image:
	"""Remove noise from an image (src) using a scale model and an alpha model.

	Args:
	----
		args (argparse.Namespace): argparse namespace containing config such as the block_size
		src (Image.Image): Pillow image to remove noise from
		model (Chain): model for scaling
		should_print (bool): Flag to enable print to console

	Returns:
	-------
		Image.Image: Pillow image with noise removed

	"""
	dst, alpha = split_alpha(src, model, should_print=should_print)
	if should_print:
		print(f"Level {args.noise_level} denoising...", end=" ", flush=True)
	if args.tta:
		dst = reconstruct.image_tta(dst, model, args.tta_level, args.block_size, args.batch_size)
	else:
		dst = reconstruct.image(dst, model, args.block_size, args.batch_size)
	if model.inner_scale != 1:
		dst = dst.resize((src.size[0], src.size[1]), Image.LANCZOS)
	if should_print:
		print("OK")
	if alpha is not None:
		dst.putalpha(alpha)
	return dst


def upscale_image(
	args: argparse.Namespace,
	src: Image.Image,
	scale_model: Chain,
	alpha_model: Chain | None = None,
	*,
	should_print: bool = True,
) -> Image.Image:
	"""Upscale an image (src) using a scale model and an alpha model.

	Args:
	----
		args (argparse.Namespace): argparse namespace containing config such as the scale_ratio and
		block size
		src (Image.Image): Pillow image to upscale
		scale_model (Chain): model to use for scaling
		alpha_model (Chain, optional): model to use for alpha. Defaults to None.
		should_print (bool): flag to enable output to console

	Returns:
	-------
		Image.Image: upscaled Pillow image

	"""
	dst, alpha = split_alpha(src, scale_model, should_print=should_print)
	for i in range(int(np.ceil(np.log2(args.scale_ratio)))):
		if should_print:
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
		if should_print:
			print("OK")
	dst_w = int(np.round(src.size[0] * args.scale_ratio))
	dst_h = int(np.round(src.size[1] * args.scale_ratio))
	if dst_w != dst.size[0] or dst_h != dst.size[1]:
		if should_print:
			print("Resizing...", end=" ", flush=True)
		dst = dst.resize((dst_w, dst_h), Image.LANCZOS)
		if should_print:
			print("OK")
	if alpha is not None:
		if alpha.size[0] != dst_w or alpha.size[1] != dst_h:
			alpha = alpha.resize((dst_w, dst_h), Image.LANCZOS)
		dst.putalpha(alpha)
	return dst


def split_alpha(
	src: Image.Image, model: Chain, *, should_print: bool = True
) -> tuple[Image.Image, Image.Image | None]:
	"""Split the image into an rgb, and alpha tuple.

	:param Image.Image src: image
	:param Chain model: model to use
	:param bool should_print: print to stdout?, defaults to True
	:return tuple[Image.Image, Image.Image | None]: rgb, and alpha tuple
	"""
	alpha = None
	if src.mode in ("L", "RGB", "P"):
		srcRGBA = src.convert("RGBA")
		alphas = [x[1][-1] for x in srcRGBA.getcolors(src.size[0] * src.size[1])]
		if any(x < 255 for x in alphas):
			if should_print:
				print(f"Alpha channel detected in image with mode={src.mode}")
			alpha = srcRGBA.split()[-1]
	rgb = src.convert("RGB")
	if src.mode in ("LA", "RGBA"):
		if should_print:
			print("Splitting alpha channel...", end=" ", flush=True)
		alpha = src.split()[-1]
		rgb = iproc.alpha_make_border(rgb, alpha, model)
		if should_print:
			print("OK")
	return rgb, alpha


def load_models(args: argparse.Namespace) -> dict[str, Chain]:
	"""Load models using a args config.

	Args:
	----
		args (argparse.Namespace): argparse namespace containing config such as the arch and color

	Returns:
	-------
		dict[str, Chain]: Mapping of model names to Chain models

	"""
	ch = 3 if args.color == "rgb" else 1
	if args.model_dir is None:
		model_dir = THISDIR / f"models/{args.arch.lower()}"
	else:
		model_dir = Path(args.model_dir)

	models = {}
	flag = False
	if args.method == "noise_scale":
		model_name = f"anime_style_noise{args.noise_level}_scale_{args.color}.npz"
		model_path = model_dir / model_name
		if model_path.exists():
			models["noise_scale"] = srcnn.archs[args.arch](ch)
			load_npz(model_path, models["noise_scale"])
			alpha_model_name = f"anime_style_scale_{args.color}.npz"
			alpha_model_path = model_dir / alpha_model_name
			models["alpha"] = srcnn.archs[args.arch](ch)
			load_npz(alpha_model_path, models["alpha"])
		else:
			flag = True
	if args.method == "scale" or flag:
		model_name = f"anime_style_scale_{args.color}.npz"
		model_path = model_dir / model_name
		models["scale"] = srcnn.archs[args.arch](ch)
		load_npz(model_path, models["scale"])
	if args.method == "noise" or flag:
		model_name = f"anime_style_noise{args.noise_level}_{args.color}.npz"
		model_path = model_dir / model_name
		if not model_path.exists():
			model_name = f"anime_style_noise{args.noise_level}_scale_{args.color}.npz"
			model_path = model_dir / model_name
		models["noise"] = srcnn.archs[args.arch](ch)
		load_npz(model_path, models["noise"])

	if args.gpu >= 0:
		cuda.check_cuda_available()
		cuda.get_device(args.gpu).use()
		for model in models.values():
			model.to_gpu()
	return models


def run(
	input_img_path: str = "images/small.png",
	output_img_path: str = "./",
	*,
	gpu: int = -1,
	quality: int | None = None,
	model_dir: str | None = None,
	scale_ratio: float = 2.0,
	# tta=False,  # Not sure how to add this.
	batch_size: int = 16,
	block_size: int = 128,
	extension: str = "png",
	arch: str = "VGG7",
	method: str = "scale",
	noise_level: int = 1,
	color: str = "rgb",
	tta_level: int = 8,
	width: int = 0,
	height: int = 0,
	shorter_side: int = 0,
	longer_side: int = 0,
	should_print: bool = True,
) -> None:  # pragma: no cover
	"""Run waifu2x using mostly the same inputs as CLI ones.

	:param str input_img_path: Input image/ directory, defaults to "images/small.png"
	:param str output_img_path: Directory to write output images to, defaults to "./"
	:param int gpu: CUDA enabled GPU to use, defaults to -1
	:param int | None quality: Set the quality of output images 1-100 (None=100), defaults to None
	:param str | None model_dir: Specify a custom directory containing models, defaults to None
	:param float scale_ratio: Specify a scale, defaults to 2.0
	:param int batch_size: _description_, defaults to 16
	:param int block_size: _description_, defaults to 128
	:param str extension: Select output extension png/webp
	:param str arch: _description_, defaults to "VGG7"
	:param str method: _description_, defaults to "scale"
	:param int noise_level: _description_, defaults to 1
	:param str color: _description_, defaults to "rgb"
	:param int tta_level: _description_, defaults to 8
	:param int width: _description_, defaults to 0
	:param int height: _description_, defaults to 0
	:param int shorter_side: _description_, defaults to 0
	:param int longer_side: _description_, defaults to 0
	:param bool should_print: _description_, defaults to True
	:raises ValueError: Output file extension not supported
	"""
	# fmt:off
	p = argparse.ArgumentParser(description="Chainer implementation of waifu2x")
	p.add_argument("--gpu", "-g", type=int, default=gpu, help="CUDA enabled GPU to use")
	p.add_argument("--input", "-i", default=input_img_path, help="Input image/ directory")
	p.add_argument("--output", "-o", default=output_img_path, help="Directory to write output images to")
	p.add_argument("--quality", "-q", type=int, default=quality, help="Set the quality of output images 1-100 (None=100)")
	p.add_argument("--model_dir", "-d", default=model_dir, help="Specify a custom directory containing models")
	p.add_argument("--scale_ratio", "-s", type=float, default=scale_ratio, help="Specify a scale")
	p.add_argument("--tta", "-t", action="store_true")
	p.add_argument("--batch_size", "-b", type=int, default=batch_size)
	p.add_argument("--block_size", "-l", type=int, default=block_size)
	p.add_argument("--extension", "-e", default=extension, choices=["png", "webp"], help="Select output extension png/webp")
	p.add_argument("--arch", "-a", default=arch, choices=["VGG7", "0", "UpConv7", "1", "ResNet10", "2", "UpResNet10", "3"])
	p.add_argument("--method", "-m", default=method, choices=["noise", "scale", "noise_scale"])
	p.add_argument("--noise_level", "-n", type=int, default=noise_level, choices=[0, 1, 2, 3])
	p.add_argument("--color", "-c", default=color, choices=["y", "rgb"])
	p.add_argument("--tta_level", "-T", type=int, default=tta_level, choices=[2, 4, 8])
	g = p.add_mutually_exclusive_group()
	g.add_argument("--width", "-W", type=int, default=width)
	g.add_argument("--height", "-H", type=int, default=height)
	g.add_argument("--shorter_side", "-S", type=int, default=shorter_side)
	g.add_argument("--longer_side", "-L", type=int, default=longer_side)
	# fmt:on

	args = p.parse_args()
	if args.arch in srcnn.table:
		args.arch = srcnn.table[args.arch]

	models = load_models(args)

	input_exts = [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"]
	output_exts = [".png", ".webp"]

	# Get filelist
	inputpath = Path(args.input)
	if inputpath.is_dir():
		filelist = utils.load_filelist(args.input)
	else:
		if inputpath.suffix not in input_exts:
			msg = "Input suffix is not supported!"
			raise ValueError(msg)
		filelist = [args.input]

	# Output dir/ file
	outsuffix = f".{extension}"
	outputpath = Path(args.output)
	if outputpath.is_dir():
		outdir = args.output
	else:
		outdir = outputpath.parent.as_posix()
		outsuffix = outputpath.suffix

	outfile = None
	if len(filelist) == 1 and not outputpath.is_dir():
		outfile = Path(args.output).name

	for infile in filelist:
		# File Exists?
		inpath = Path(infile)
		if not inpath.exists():
			p.print_help()
			sys.exit(1)

		if inpath.suffix in input_exts:
			src = Image.open(infile)
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

			outname = inpath.name
			outname += f"_(tta{args.tta_level})" if args.tta else "_"
			if "noise_scale" in models:
				outname += f"(noise{args.noise_level}_scale{args.scale_ratio:.1f}x)"
				dst = upscale_image(
					args, dst, models["noise_scale"], models["alpha"], should_print=should_print
				)
			else:
				if "noise" in models:
					outname += f"(noise{args.noise_level})"
					dst = denoise_image(args, dst, models["noise"], should_print=should_print)
				if "scale" in models:
					outname += f"(scale{args.scale_ratio:.1f}x)"
					dst = upscale_image(args, dst, models["scale"], should_print=should_print)
			if should_print:
				print(f"Elapsed time: {time.time() - start:.6f} sec")

			if outsuffix not in output_exts:
				msg = "Output suffix is not supported!"
				raise ValueError(msg)

			outname += f"({args.arch}_{args.color}){outsuffix}"

			if outfile is not None:
				outname = outfile

			outpath = Path(outdir, outname)

			lossless = args.quality is None
			quality = 100 if lossless else args.quality
			icc_profile = src.info.get("icc_profile")
			icc_profile = "" if icc_profile is None else icc_profile
			dst.convert(src.mode).save(
				outpath, quality=quality, lossless=lossless, icc_profile=icc_profile
			)
			if should_print:
				print(f"Saved as '{outpath}'")


if __name__ == "__main__":  # pragma: no cover
	main()
