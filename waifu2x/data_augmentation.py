"""Module contains functions for image processing including applying filters like
unsharp mask, adding color noise, flipping, scaling, and shifting images.

Dependencies:
	- numpy (np)
	- Pillow (PIL)
	- iproc

Note:
----
	- Functions in this module are designed to work with numpy arrays representing images.


"""

from __future__ import annotations

import random

import numpy as np
from PIL import Image, ImageFilter

from waifu2x import iproc


def unsharp_mask(src: np.ndarray, p: float) -> np.ndarray:
	"""Apply unsharp mask filter to the input image array.

	Args:
	----
	src (np.ndarray): Input image array.
	p (float): Probability of applying the filter.

	Returns:
	-------
	np.ndarray: Processed image array.

	"""
	if np.random.uniform() < p:
		tmp = Image.fromarray(src)
		percent = random.randint(10, 90)
		threshold = random.randint(0, 5)
		mask = ImageFilter.UnsharpMask(percent=percent, threshold=threshold)
		return np.array(tmp.filter(mask), dtype=np.uint8)
	return src


def color_noise(src: np.ndarray, p: float, factor: float = 0.1) -> np.ndarray:
	"""
	Apply color noise to the input image array.

	Args:
	----
	src (np.ndarray): Input image array.
	p (float): Probability of applying the noise.
	factor (float): Noise factor.

	Returns:
	-------
	np.ndarray: Processed image array.

	"""
	if np.random.uniform() < p:
		tmp = np.array(src, dtype=np.float32) / 255.0
		scale = np.random.normal(0, factor, 3)
		ce, cv = iproc.pcacov(tmp)
		noise = cv.dot(ce.T * scale)[np.newaxis, np.newaxis, :]
		dst = np.clip(tmp + noise, 0, 1) * 255
		return dst.astype(np.uint8)
	return src


def flip(src: np.ndarray) -> np.ndarray:
	"""
	Flip the input image array.

	Args:
	----
	src (np.ndarray): Input image array.

	Returns:
	-------
	np.ndarray: Processed image array.

	"""
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
	"""Scale down the input image array by half.

	Args:
	----
	src (np.ndarray): Input image array.
	p (np.ndarray): Probability array.

	Returns:
	-------
	np.ndarray: Processed image array.

	"""
	if np.random.uniform() < p:
		filters = ("box", "box", "blackman", "cubic", "lanczos")
		rand = random.randint(0, len(filters) - 1)
		return iproc.scale(src, 0.5, filters[rand])
	return src


def shift_1px(src: np.ndarray) -> np.ndarray:
	"""Shift the input image array by 1 pixel.

	Args:
	----
	- src (np.ndarray): Input image array.

	Returns:
	-------
	- np.ndarray: Shifted image array.

	"""
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
	return src[y_shift : y_shift + h, x_shift : x_shift + w, :]
