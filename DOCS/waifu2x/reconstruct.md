# reconstruct

> Auto-generated documentation for [waifu2x.reconstruct](../../waifu2x/reconstruct.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / reconstruct
    - [blockwise](#blockwise)
    - [get_tta_patterns](#get_tta_patterns)
    - [image](#image)
    - [image_tta](#image_tta)
    - [inv](#inv)

## blockwise

[[find in source code]](../../waifu2x/reconstruct.py#L15)

```python
def blockwise(src, model, block_size, batch_size):
```

## get_tta_patterns

[[find in source code]](../../waifu2x/reconstruct.py#L70)

```python
def get_tta_patterns(src, n):
```

## image

[[find in source code]](../../waifu2x/reconstruct.py#L124)

```python
def image(src, model, block_size, batch_size):
```

## image_tta

[[find in source code]](../../waifu2x/reconstruct.py#L91)

```python
def image_tta(src, model, tta_level, block_size, batch_size):
```

## inv

[[find in source code]](../../waifu2x/reconstruct.py#L63)

```python
def inv(rot, flip=False):
```
