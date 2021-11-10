# reconstruct

> Auto-generated documentation for [waifu2x.reconstruct](../../waifu2x/reconstruct.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / reconstruct
    - [blockwise](#blockwise)
    - [get_tta_patterns](#get_tta_patterns)
    - [image](#image)
    - [image_tta](#image_tta)
    - [inv](#inv)

## blockwise

[[find in source code]](../../waifu2x/reconstruct.py#L17)

```python
def blockwise(src, model, block_size: int, batch_size: int):
```

## get_tta_patterns

[[find in source code]](../../waifu2x/reconstruct.py#L71)

```python
def get_tta_patterns(src, n: int):
```

## image

[[find in source code]](../../waifu2x/reconstruct.py#L125)

```python
def image(src, model, block_size: int, batch_size: int) -> Image.Image:
```

## image_tta

[[find in source code]](../../waifu2x/reconstruct.py#L92)

```python
def image_tta(src, model, tta_level: int, block_size: int, batch_size: int):
```

## inv

[[find in source code]](../../waifu2x/reconstruct.py#L65)

```python
def inv(rot: int, flip: bool = False):
```
