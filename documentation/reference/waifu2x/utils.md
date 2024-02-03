# Utils

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Utils

> Auto-generated documentation for [waifu2x.utils](../../../waifu2x/utils.py) module.

- [Utils](#utils)
  - [Namespace](#namespace)
    - [Namespace().__repr__](#namespace()__repr__)
    - [Namespace().__str__](#namespace()__str__)
    - [Namespace().append](#namespace()append)
  - [get_config](#get_config)
  - [load_filelist](#load_filelist)
  - [set_random_seed](#set_random_seed)

## Namespace

[Show source in utils.py:13](../../../waifu2x/utils.py#L13)

Namespace representing a series of key value pairs. Similar to argparse.Namespace.

#### Signature

```python
class Namespace:
    def __init__(self, kwargs: dict[str, Any]) -> None: ...
```

### Namespace().__repr__

[Show source in utils.py:25](../../../waifu2x/utils.py#L25)

Get a string representation of a namespace.

#### Returns

Type: *str*
representation of a namespace

#### Signature

```python
def __repr__(self) -> str: ...
```

### Namespace().__str__

[Show source in utils.py:33](../../../waifu2x/utils.py#L33)

Get a string representation of a namespace.

#### Returns

Type: *str*
representation of a namespace

#### Signature

```python
def __str__(self) -> str: ...
```

### Namespace().append

[Show source in utils.py:40](../../../waifu2x/utils.py#L40)

Append a new value and update the internal rep.

#### Arguments

- `key` *str* - key to store a new value at
- `value` *Any* - corresponding value

#### Signature

```python
def append(self, key: str, value: Any) -> None: ...
```



## get_config

[Show source in utils.py:50](../../../waifu2x/utils.py#L50)

#### Signature

```python
def get_config(base, model, train: bool = True) -> Namespace: ...
```

#### See also

- [Namespace](#namespace)



## load_filelist

[Show source in utils.py:104](../../../waifu2x/utils.py#L104)

Get a list of files given a directory.

#### Arguments

- `directory` *str* - path to a directory
- `shuffle` *bool* - use random.shuffle to change the order of returned files, defaults to False

#### Returns

Type: *list[str]*
list of file paths

#### Signature

```python
def load_filelist(directory: str, shuffle: bool = False) -> list[str]: ...
```



## set_random_seed

[Show source in utils.py:90](../../../waifu2x/utils.py#L90)

Set a seed given an iv and a gpu index (note -1 is 'no gpu').

#### Arguments

- `seed` *float* - seed/ iv for random
- `gpu` *int* - gpu index (-1 is no gpu), defaults to -1

#### Signature

```python
def set_random_seed(seed: float, gpu: int = -1) -> None: ...
```