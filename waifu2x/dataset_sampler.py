from __future__ import annotations

import argparse
import multiprocessing
import os
from tempfile import NamedTemporaryFile

import numpy as np

from . import iproc
from .pairwise_transform import pairwise_transform


class DatasetSampler:
	def __init__(self, filelist, config):
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

	def __del__(self):
		self.finalize()

	def finalize(self):
		if self._running:
			self._finalized.set()
			garbage = self._queue.get(timeout=0.5)
			self.worker.join()
			os.remove(garbage)

	def reload_switch(self, init: bool = True):
		self._init = init
		self._reload = True

	def _init_process(self):
		self._queue = multiprocessing.Queue()
		self._finalized = multiprocessing.Event()
		args = [self.filelist, self.config, self._queue, self._finalized]
		self.worker = multiprocessing.Process(target=_worker, args=args)
		self.worker.daemon = True
		self.worker.start()
		self._running = True

	def wait(self):
		if self._running and self.cache_name is None:
			self.cache_name = self._queue.get()
			self.worker.join()
			self._running = False

	def get(self):
		if self._reload:
			if self._running and self.cache_name is None:
				self.cache_name = self._queue.get()
				self.worker.join()
				self._running = False
			with np.load(self.cache_name) as cached_arr:
				self.dataset = cached_arr["x"], cached_arr["y"]
			os.remove(self.cache_name)
			if self._init:
				self._init_process()
			self.cache_name = None
			self._reload = False
		return self.dataset


def _worker(filelist: list[str], args: argparse.Namespace, queue, finalized):
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
