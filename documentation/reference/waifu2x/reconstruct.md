# Reconstruct

> Auto-generated documentation for [waifu2x.reconstruct](../../../waifu2x/reconstruct.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../MODULES.md#waifu2x-modules) / [Waifu2x](index.md#waifu2x) / Reconstruct
    - [blockwise](#blockwise)
    - [get_tta_patterns](#get_tta_patterns)
    - [image](#image)
    - [image_tta](#image_tta)
    - [inv](#inv)

## blockwise

[[find in source code]](../../../waifu2x/reconstruct.py#L17)

```python
def blockwise(
    src: np.ndarray,
    model: chainer.Chain,
    block_size: int,
    batch_size: int,
):
```

## get_tta_patterns

[[find in source code]](../../../waifu2x/reconstruct.py#L71)

```python
def get_tta_patterns(src: np.ndarray, n: int):
```

## image

[[find in source code]](../../../waifu2x/reconstruct.py#L127)

```python
def image(src, model, block_size: int, batch_size: int) -> Image.Image:
```

## image_tta

[[find in source code]](../../../waifu2x/reconstruct.py#L92)

```python
def image_tta(
    src: Image.Image,
    model: chainer.Chain,
    tta_level: int,
    block_size: int,
    batch_size: int,
):
```

## inv

[[find in source code]](../../../waifu2x/reconstruct.py#L65)

```python
def inv(rot: int, flip: bool = False):
```
