# utils

> Auto-generated documentation for [waifu2x.utils](../../waifu2x/utils.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / utils
    - [Namespace](#namespace)
        - [Namespace().append](#namespaceappend)
    - [get_config](#get_config)
    - [load_filelist](#load_filelist)
    - [set_random_seed](#set_random_seed)

## Namespace

[[find in source code]](../../waifu2x/utils.py#L9)

```python
class Namespace():
    def __init__(kwargs):
```

### Namespace().append

[[find in source code]](../../waifu2x/utils.py#L21)

```python
def append(key, value):
```

## get_config

[[find in source code]](../../waifu2x/utils.py#L26)

```python
def get_config(base, model, train: bool = True):
```

## load_filelist

[[find in source code]](../../waifu2x/utils.py#L75)

```python
def load_filelist(directory: str, shuffle: bool = False):
```

## set_random_seed

[[find in source code]](../../waifu2x/utils.py#L66)

```python
def set_random_seed(seed, gpu: int = -1):
```
