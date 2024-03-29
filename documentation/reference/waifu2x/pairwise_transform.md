# Pairwise Transform

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Pairwise Transform

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

[Show source in pairwise_transform.py:90](../../../waifu2x/pairwise_transform.py#L90)

#### Signature

```python
def active_cropping(x, y, ly, size: int, scale_: int, p, tries: int): ...
```



## crop_if_large

[Show source in pairwise_transform.py:73](../../../waifu2x/pairwise_transform.py#L73)

#### Signature

```python
def crop_if_large(src: np.ndarray, max_size: int): ...
```



## noise

[Show source in pairwise_transform.py:39](../../../waifu2x/pairwise_transform.py#L39)

#### Signature

```python
def noise(src: np.ndarray, p: np.ndarray, p_chroma, level: int): ...
```



## noise_scale

[Show source in pairwise_transform.py:58](../../../waifu2x/pairwise_transform.py#L58)

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
): ...
```



## pairwise_transform

[Show source in pairwise_transform.py:124](../../../waifu2x/pairwise_transform.py#L124)

#### Signature

```python
def pairwise_transform(src: np.ndarray, args: argparse.Namespace): ...
```



## preprocess

[Show source in pairwise_transform.py:81](../../../waifu2x/pairwise_transform.py#L81)

#### Signature

```python
def preprocess(src: np.ndarray, args: argparse.Namespace): ...
```



## scale

[Show source in pairwise_transform.py:47](../../../waifu2x/pairwise_transform.py#L47)

#### Signature

```python
def scale(src: np.ndarray, filters, bmin, bmax, scale_): ...
```