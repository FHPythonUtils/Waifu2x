# Pairwise Transform

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Pairwise Transform

> Auto-generated documentation for [waifu2x.pairwise_transform](../../../waifu2x/pairwise_transform.py) module.

- [Pairwise Transform](#pairwise-transform)
  - [active_cropping](#active_cropping)
  - [crop_if_large](#crop_if_large)
  - [noise](#noise)
  - [noise_scale](#noise_scale)
  - [pairwise_transform](#pairwise_transform)
  - [preprocess](#preprocess)
  - [scale](#scale)

## active_cropping

[Show source in pairwise_transform.py:96](../../../waifu2x/pairwise_transform.py#L96)

#### Signature

```python
def active_cropping(x, y, ly, size: int, scale_: int, p, tries: int):
    ...
```



## crop_if_large

[Show source in pairwise_transform.py:77](../../../waifu2x/pairwise_transform.py#L77)

#### Signature

```python
def crop_if_large(src: np.ndarray, max_size: int):
    ...
```



## noise

[Show source in pairwise_transform.py:40](../../../waifu2x/pairwise_transform.py#L40)

#### Signature

```python
def noise(src: np.ndarray, p: np.ndarray, p_chroma, level: int):
    ...
```



## noise_scale

[Show source in pairwise_transform.py:61](../../../waifu2x/pairwise_transform.py#L61)

#### Signature

```python
def noise_scale(
    src: np.ndarray,
    filters,
    bmin: float,
    bmax: float,
    scale_,
    p: np.ndarray,
    p_chroma,
    level: int,
):
    ...
```



## pairwise_transform

[Show source in pairwise_transform.py:128](../../../waifu2x/pairwise_transform.py#L128)

#### Signature

```python
def pairwise_transform(src: np.ndarray, args: argparse.Namespace):
    ...
```



## preprocess

[Show source in pairwise_transform.py:86](../../../waifu2x/pairwise_transform.py#L86)

#### Signature

```python
def preprocess(src: np.ndarray, args: argparse.Namespace):
    ...
```



## scale

[Show source in pairwise_transform.py:49](../../../waifu2x/pairwise_transform.py#L49)

#### Signature

```python
def scale(src: np.ndarray, filters, bmin, bmax, scale_):
    ...
```


