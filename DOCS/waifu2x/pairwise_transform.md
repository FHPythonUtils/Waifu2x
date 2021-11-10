# pairwise_transform

> Auto-generated documentation for [waifu2x.pairwise_transform](../../waifu2x/pairwise_transform.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / pairwise_transform
    - [active_cropping](#active_cropping)
    - [crop_if_large](#crop_if_large)
    - [noise](#noise)
    - [noise_scale](#noise_scale)
    - [pairwise_transform](#pairwise_transform)
    - [preprocess](#preprocess)
    - [scale](#scale)

## active_cropping

[[find in source code]](../../waifu2x/pairwise_transform.py#L94)

```python
def active_cropping(x, y, ly, size: int, scale_: int, p, tries: int):
```

## crop_if_large

[[find in source code]](../../waifu2x/pairwise_transform.py#L75)

```python
def crop_if_large(src, max_size: int):
```

## noise

[[find in source code]](../../waifu2x/pairwise_transform.py#L40)

```python
def noise(src, p, p_chroma, level: int):
```

## noise_scale

[[find in source code]](../../waifu2x/pairwise_transform.py#L61)

```python
def noise_scale(src, filters, bmin, bmax, scale_, p, p_chroma, level: int):
```

## pairwise_transform

[[find in source code]](../../waifu2x/pairwise_transform.py#L126)

```python
def pairwise_transform(src, args: argparse.Namespace):
```

## preprocess

[[find in source code]](../../waifu2x/pairwise_transform.py#L84)

```python
def preprocess(src, args: argparse.Namespace):
```

## scale

[[find in source code]](../../waifu2x/pairwise_transform.py#L49)

```python
def scale(src, filters, bmin, bmax, scale_):
```
