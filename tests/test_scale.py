import sys
from argparse import Namespace
from pathlib import Path

from imgcompare import imgcompare
from PIL import Image

THISDIR = str(Path(__file__).resolve().parent)
sys.path.insert(0, str(Path(THISDIR).parent))

from waifu2x import load_models, upscale_image

args = Namespace(
	color="rgb",
	model_dir=None,
	arch="VGG7",
	method="scale",
	noise_level=1,
	gpu=-1,
	scale_ratio=2.0,
	tta=False,
	block_size=128,
	batch_size=16,
)
models = load_models(args)


def test_background_png():
	"""test_background_png"""
	src = Image.open(f"{THISDIR}/data/background.png")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	# dst.convert(src.mode).save(f"{THISDIR}/data/background_expected.png")
	assert imgcompare.is_equal(
		dst,
		f"{THISDIR}/data/background_expected.png",
		tolerance=0.2,
	)


def test_background_jpg():
	"""test_background_jpg"""
	src = Image.open(f"{THISDIR}/data/background.jpg")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	# dst.convert(src.mode).save(f"{THISDIR}/data/background_expected.jpg.png")
	assert imgcompare.is_equal(
		dst,
		f"{THISDIR}/data/background_expected.jpg.png",
		tolerance=0.2,
	)


def test_foreground_png():
	"""test_foreground_png"""
	src = Image.open(f"{THISDIR}/data/foreground.png")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	# dst.convert(src.mode).save(f"{THISDIR}/data/foreground_expected.png")
	assert imgcompare.is_equal(
		dst,
		f"{THISDIR}/data/foreground_expected.png",
		tolerance=0.2,
	)


def test_foreground_jpg():
	"""test_foreground_jpg"""
	src = Image.open(f"{THISDIR}/data/foreground.jpg")
	dst = src.copy()
	dst = upscale_image(args, dst, models["scale"])
	# dst.convert(src.mode).save(f"{THISDIR}/data/foreground_expected.jpg.png")
	assert imgcompare.is_equal(
		dst,
		f"{THISDIR}/data/foreground_expected.jpg.png",
		tolerance=0.2,
	)


if __name__ == "__main__":  # pragma: no cover
	test_background_png()
	test_background_jpg()
	test_foreground_png()
	test_foreground_jpg()
