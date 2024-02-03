"""Utility methods used in the waifu2x module."""

from __future__ import annotations

import os
import random
from pathlib import Path
from typing import Any

import numpy as np


class Namespace:
	"""Namespace representing a series of key value pairs. Similar to argparse.Namespace."""

	def __init__(self, kwargs: dict[str, Any]) -> None:
		"""Namespace representing a series of key value pairs. Similar to argparse.Namespace.

		:param dict[str, Any] kwargs: initial values
		"""
		self.kwargs = kwargs
		for key in kwargs:
			setattr(self, key, kwargs[key])

	def __repr__(self) -> str:
		"""Get a string representation of a namespace.

		:return str:  representation of a namespace
		"""
		parts = [f"{key}={self.kwargs[key]}" for key in self.kwargs]
		return ", ".join(parts)

	def __str__(self) -> str:
		"""Get a string representation of a namespace.

		:return str:  representation of a namespace
		"""
		return self.__repr__()

	def append(self, key: str, value: Any) -> None:
		"""Append a new value and update the internal rep.

		:param str key: key to store a new value at
		:param Any value: corresponding value
		"""
		self.kwargs[key] = value
		setattr(self, key, value)


def get_config(base, model, *, train: bool = True) -> Namespace:
	ch = model.ch
	offset = model.offset
	inner_scale = model.inner_scale
	crop_size = base.out_size + offset * 2
	in_size = crop_size // inner_scale

	if train:
		max_size = base.max_size
		patches = base.patches
	else:
		max_size = 0
		coeff = (1 - base.validation_rate) / base.validation_rate
		patches = int(round(base.validation_crop_rate * coeff * base.patches))

	config = {
		"ch": ch,
		"method": base.method,
		"noise_level": base.noise_level,
		"nr_rate": base.nr_rate,
		"chroma_subsampling_rate": base.chroma_subsampling_rate,
		"offset": offset,
		"crop_size": crop_size,
		"in_size": in_size,
		"out_size": base.out_size,
		"inner_scale": inner_scale,
		"max_size": max_size,
		"active_cropping_rate": base.active_cropping_rate,
		"active_cropping_tries": base.active_cropping_tries,
		"random_half_rate": base.random_half_rate,
		"random_color_noise_rate": base.random_color_noise_rate,
		"random_unsharp_mask_rate": base.random_unsharp_mask_rate,
		"patches": patches,
		"downsampling_filters": base.downsampling_filters,
		"resize_blur_min": base.resize_blur_min,
		"resize_blur_max": base.resize_blur_max,
	}
	return Namespace(config)


def set_random_seed(seed: float, gpu: int = -1) -> None:
	"""Set a seed given an iv and a gpu index (note -1 is 'no gpu').

	:param float seed: seed/ iv for random
	:param int gpu: gpu index (-1 is no gpu), defaults to -1
	"""
	random.seed(seed)
	np.random.seed(seed)
	if gpu >= 0:
		import cupy

		cupy.random.seed(seed)


def load_filelist(directory: str, *, shuffle: bool = False) -> list[str]:
	"""Get a list of files given a directory.

	:param str directory: path to a directory
	:param bool shuffle: use random.shuffle to change the order of returned files, defaults to False
	:return list[str]: list of file paths
	"""
	files = os.listdir(directory)
	datalist = []
	for file in files:
		path = Path(directory) / file
		if path.is_file():
			datalist.append(path.as_posix())
	if shuffle:
		random.shuffle(datalist)
	return datalist
