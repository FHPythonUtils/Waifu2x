# Pairwise Transform

> Auto-generated documentation for [waifu2x.pairwise_transform](../../../waifu2x/pairwise_transform.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../MODULES.md#waifu2x-modules) / [Waifu2x](index.md#waifu2x) / Pairwise Transform
    - [active_cropping](#active_cropping)
    - [crop_if_large](#crop_if_large)
    - [noise](#noise)
    - [noise_scale](#noise_scale)
    - [pairwise_transform](#pairwise_transform)
    - [preprocess](#preprocess)
    - [scale](#scale)

## active_cropping

[[find in source code]](../../../waifu2x/pairwise_transform.py#L96)

```python
def active_cropping(x, y, ly, size: int, scale_: int, p, tries: int):
```

## crop_if_large

[[find in source code]](../../../waifu2x/pairwise_transform.py#L77)

```python
def crop_if_large(src: np.ndarray, max_size: int):
```

## noise

[[find in source code]](../../../waifu2x/pairwise_transform.py#L40)

```python
def noise(src: np.ndarray, p: np.ndarray, p_chroma, level: int):
```

## noise_scale

[[find in source code]](../../../waifu2x/pairwise_transform.py#L61)

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
```

## pairwise_transform

[[find in source code]](../../../waifu2x/pairwise_transform.py#L128)

```python
def pairwise_transform(src: np.ndarray, args: argparse.Namespace):
```

## preprocess

[[find in source code]](../../../waifu2x/pairwise_transform.py#L86)

```python
def preprocess(src: np.ndarray, args: argparse.Namespace):
```

## scale

[[find in source code]](../../../waifu2x/pairwise_transform.py#L49)

```python
def scale(src: np.ndarray, filters, bmin, bmax, scale_):
```
