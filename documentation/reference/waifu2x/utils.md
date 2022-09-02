# Utils

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Utils

> Auto-generated documentation for [waifu2x.utils](../../../waifu2x/utils.py) module.

- [Utils](#utils)
  - [Namespace](#namespace)
    - [Namespace().append](#namespace()append)
  - [get_config](#get_config)
  - [load_filelist](#load_filelist)
  - [set_random_seed](#set_random_seed)

## Namespace

[Show source in utils.py:9](../../../waifu2x/utils.py#L9)

#### Signature

```python
class Namespace:
    def __init__(self, kwargs):
        ...
```

### Namespace().append

[Show source in utils.py:21](../../../waifu2x/utils.py#L21)

#### Signature

```python
def append(self, key, value):
    ...
```



## get_config

[Show source in utils.py:26](../../../waifu2x/utils.py#L26)

#### Signature

```python
def get_config(base, model, train: bool = True):
    ...
```



## load_filelist

[Show source in utils.py:75](../../../waifu2x/utils.py#L75)

#### Signature

```python
def load_filelist(directory: str, shuffle: bool = False):
    ...
```



## set_random_seed

[Show source in utils.py:66](../../../waifu2x/utils.py#L66)

#### Signature

```python
def set_random_seed(seed, gpu: int = -1):
    ...
```


