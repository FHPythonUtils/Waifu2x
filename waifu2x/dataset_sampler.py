"""Module for dataset sampling and processing.

This module provides functionality for sampling datasets. It includes a class `DatasetSampler` for
managing dataset sampling processes and a helper function `_worker` for performing dataset sampling
in a separate process.


Note:
----
	- The `DatasetSampler` class manages the dataset sampling process, while the `_worker`
	function performs the actual sampling.
	- The module relies on other modules and functions for image processing and dataset
	transformation.


"""

from __future__ import annotations

import argparse
import multiprocessing
from pathlib import Path
from tempfile import NamedTemporaryFile

import numpy as np

from waifu2x import iproc
from waifu2x.pairwise_transform import pairwise_transform


class DatasetSampler:
	"""Class for sampling datasets for training or testing purposes.

	Args:
	----
		filelist (list[str]): List of file paths.
		config (argparse.Namespace): Configuration settings.

	Attributes:
	----------
		filelist (list[str]): List of file paths.
		config (argparse.Namespace): Configuration settings.
		worker (multiprocessing.Process): Worker process.
		dataset (tuple): Dataset containing input and output arrays.
		cache_name (str): Name of the cached file.
		_queue (multiprocessing.Queue): Communication queue.
		_finalized (multiprocessing.Event): Event for finalizing the process.
		_init (bool): Flag indicating initialization status.
		_reload (bool): Flag indicating whether to reload the dataset.
		_running (bool): Flag indicating whether the process is running.

	Methods:
	-------
		finalize(): Finalizes the dataset sampling process.
		reload_switch(init: bool = True): Switches the reload state.
		_init_process(): Initializes the sampling process.
		wait(): Waits for the process to complete.
		get(): Retrieves the dataset.

	"""

	def __init__(self, filelist: list[str], config: argparse.Namespace) -> None:
		"""Class for sampling datasets for training or testing purposes.

		Args:
		----
			filelist (list[str]): List of file paths.
			config (argparse.Namespace): Configuration settings.


		"""

		self.filelist = filelist
		self.config = config

		self.worker = None
		self.dataset = None
		self.cache_name = None
		self._queue = None
		self._finalized = None
		self._init = False
		self._reload = True
		self._running = False

		self._init_process()

	def __del__(self) -> None:
		self.finalize()

	def finalize(self) -> None:
		"""Finalize the dataset sampling process."""
		if self._running:
			self._finalized.set()
			garbage = self._queue.get(timeout=0.5)
			self.worker.join()
			Path.unlink(Path(garbage))

	def reload_switch(self, *, init: bool = True) -> None:
		"""Switches the reload state."""
		self._init = init
		self._reload = True

	def _init_process(self) -> None:
		"""Initialize the sampling process."""
		self._queue = multiprocessing.Queue()
		self._finalized = multiprocessing.Event()
		args = [self.filelist, self.config, self._queue, self._finalized]
		self.worker = multiprocessing.Process(target=_worker, args=args)
		self.worker.daemon = True
		self.worker.start()
		self._running = True

	def wait(self) -> None:
		"""Wait for the process to complete."""
		if self._running and self.cache_name is None:
			self.cache_name = self._queue.get()
			self.worker.join()
			self._running = False

	def get(self):
		"""Retrieve the dataset."""
		if self._reload:
			if self._running and self.cache_name is None:
				self.cache_name = self._queue.get()
				self.worker.join()
				self._running = False
			with np.load(self.cache_name) as cached_arr:
				self.dataset = cached_arr["x"], cached_arr["y"]
			Path.unlink(Path(self.cache_name))
			if self._init:
				self._init_process()
			self.cache_name = None
			self._reload = False
		return self.dataset


def _worker(filelist: list[str], args: argparse.Namespace, queue, finalized) -> None:
	"""Worker function for dataset sampling.

	Args:
	----
		filelist (list[str]): List of file paths.
		args (argparse.Namespace): Command-line arguments.
		queue (multiprocessing.Queue): Communication queue.
		finalized (multiprocessing.Event): Event for finalizing the process.

	"""
	sample_size = args.patches * len(filelist)
	x = np.zeros((sample_size, args.ch, args.in_size, args.in_size), dtype=np.uint8)
	y = np.zeros((sample_size, args.ch, args.out_size, args.out_size), dtype=np.uint8)

	for i, file in enumerate(filelist):
		if finalized.is_set():
			break
		img = iproc.read_image_rgb_uint8(file)
		xc_batch, yc_batch = pairwise_transform(img, args)
		x[args.patches * i : args.patches * (i + 1)] = xc_batch[:]
		y[args.patches * i : args.patches * (i + 1)] = yc_batch[:]

	with NamedTemporaryFile(delete=False) as cache:
		np.savez(cache, x=x, y=y)
		del x, y
		queue.put(cache.name)
