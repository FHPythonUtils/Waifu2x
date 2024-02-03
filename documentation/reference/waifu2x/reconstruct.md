# Reconstruct

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Reconstruct

> Auto-generated documentation for [waifu2x.reconstruct](../../../waifu2x/reconstruct.py) module.

- [Reconstruct](#reconstruct)
  - [blockwise](#blockwise)
  - [get_tta_patterns](#get_tta_patterns)
  - [image](#image)
  - [image_tta](#image_tta)
  - [inv](#inv)

## blockwise

[Show source in reconstruct.py:14](../../../waifu2x/reconstruct.py#L14)

#### Signature

```python
def blockwise(src: np.ndarray, model: Chain, block_size: int, batch_size: int): ...
```



## get_tta_patterns

[Show source in reconstruct.py:68](../../../waifu2x/reconstruct.py#L68)

#### Signature

```python
def get_tta_patterns(src: np.ndarray, n: int): ...
```



## image

[Show source in reconstruct.py:120](../../../waifu2x/reconstruct.py#L120)

#### Signature

```python
def image(src, model, block_size: int, batch_size: int) -> Image.Image: ...
```



## image_tta

[Show source in reconstruct.py:89](../../../waifu2x/reconstruct.py#L89)

#### Signature

```python
def image_tta(
    src: Image.Image, model: Chain, tta_level: int, block_size: int, batch_size: int
): ...
```



## inv

[Show source in reconstruct.py:62](../../../waifu2x/reconstruct.py#L62)

#### Signature

```python
def inv(rot: int, flip: bool = False): ...
```