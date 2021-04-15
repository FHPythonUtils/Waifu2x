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

[[find in source code]](../../waifu2x/pairwise_transform.py#L93)

```python
def active_cropping(x, y, ly, size, scale, p, tries):
```

## crop_if_large

[[find in source code]](../../waifu2x/pairwise_transform.py#L74)

```python
def crop_if_large(src, max_size):
```

## noise

[[find in source code]](../../waifu2x/pairwise_transform.py#L38)

```python
def noise(src, p, p_chroma, level):
```

## noise_scale

[[find in source code]](../../waifu2x/pairwise_transform.py#L60)

```python
def noise_scale(src, filters, bmin, bmax, scale, p, p_chroma, level):
```

## pairwise_transform

[[find in source code]](../../waifu2x/pairwise_transform.py#L121)

```python
def pairwise_transform(src, cfg):
```

## preprocess

[[find in source code]](../../waifu2x/pairwise_transform.py#L83)

```python
def preprocess(src, cfg):
```

## scale

[[find in source code]](../../waifu2x/pairwise_transform.py#L48)

```python
def scale(src, filters, bmin, bmax, scale):
```
