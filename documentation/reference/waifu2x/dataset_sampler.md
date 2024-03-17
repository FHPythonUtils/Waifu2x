# DatasetSampler

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / DatasetSampler

> Auto-generated documentation for [waifu2x.dataset_sampler](../../../waifu2x/dataset_sampler.py) module.

- [DatasetSampler](#datasetsampler)
  - [DatasetSampler](#datasetsampler-1)
    - [DatasetSampler()._init_process](#datasetsampler()_init_process)
    - [DatasetSampler().finalize](#datasetsampler()finalize)
    - [DatasetSampler().get](#datasetsampler()get)
    - [DatasetSampler().reload_switch](#datasetsampler()reload_switch)
    - [DatasetSampler().wait](#datasetsampler()wait)
  - [_worker](#_worker)

## DatasetSampler

[Show source in dataset_sampler.py:31](../../../waifu2x/dataset_sampler.py#L31)

Class for sampling datasets for training or testing purposes.

#### Arguments

----
 - `filelist` *list[str]* - List of file paths.
 - `config` *argparse.Namespace* - Configuration settings.

#### Attributes

----------
 - `filelist` *list[str]* - List of file paths.
 - `config` *argparse.Namespace* - Configuration settings.
 - `worker` *multiprocessing.Process* - Worker process.
 - `dataset` *tuple* - Dataset containing input and output arrays.
 - `cache_name` *str* - Name of the cached file.
 - `_queue` *multiprocessing.Queue* - Communication queue.
 - `_finalized` *multiprocessing.Event* - Event for finalizing the process.
 - `_init` *bool* - Flag indicating initialization status.
 - `_reload` *bool* - Flag indicating whether to reload the dataset.
 - `_running` *bool* - Flag indicating whether the process is running.

#### Methods

-------
 - `finalize()` - Finalizes the dataset sampling process.
 - `reload_switch(init` - bool = True): Switches the reload state.
 - `_init_process()` - Initializes the sampling process.
 - `wait()` - Waits for the process to complete.
 - `get()` - Retrieves the dataset.

#### Signature

```python
class DatasetSampler:
    def __init__(self, filelist: list[str], config: argparse.Namespace) -> None: ...
```

### DatasetSampler()._init_process

[Show source in dataset_sampler.py:103](../../../waifu2x/dataset_sampler.py#L103)

Initialize the sampling process.

#### Signature

```python
def _init_process(self) -> None: ...
```

### DatasetSampler().finalize

[Show source in dataset_sampler.py:90](../../../waifu2x/dataset_sampler.py#L90)

Finalize the dataset sampling process.

#### Signature

```python
def finalize(self) -> None: ...
```

### DatasetSampler().get

[Show source in dataset_sampler.py:120](../../../waifu2x/dataset_sampler.py#L120)

Retrieve the dataset.

#### Signature

```python
def get(self): ...
```

### DatasetSampler().reload_switch

[Show source in dataset_sampler.py:98](../../../waifu2x/dataset_sampler.py#L98)

Switches the reload state.

#### Signature

```python
def reload_switch(self, init: bool = True) -> None: ...
```

### DatasetSampler().wait

[Show source in dataset_sampler.py:113](../../../waifu2x/dataset_sampler.py#L113)

Wait for the process to complete.

#### Signature

```python
def wait(self) -> None: ...
```



## _worker

[Show source in dataset_sampler.py:137](../../../waifu2x/dataset_sampler.py#L137)

Worker function for dataset sampling.

#### Arguments

----
 - `filelist` *list[str]* - List of file paths.
 - `args` *argparse.Namespace* - Command-line arguments.
 - `queue` *multiprocessing.Queue* - Communication queue.
 - `finalized` *multiprocessing.Event* - Event for finalizing the process.

#### Signature

```python
def _worker(filelist: list[str], args: argparse.Namespace, queue, finalized) -> None: ...
```