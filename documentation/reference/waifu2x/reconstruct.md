# Reconstruct

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Reconstruct

> Auto-generated documentation for [waifu2x.reconstruct](../../../waifu2x/reconstruct.py) module.

- [Reconstruct](#reconstruct)
  - [blockwise](#blockwise)
  - [get_tta_patterns](#get_tta_patterns)
  - [image](#image)
  - [image_tta](#image_tta)
  - [inv](#inv)

## blockwise

[Show source in reconstruct.py:17](../../../waifu2x/reconstruct.py#L17)

#### Signature

```python
def blockwise(src: np.ndarray, model: chainer.Chain, block_size: int, batch_size: int):
    ...
```



## get_tta_patterns

[Show source in reconstruct.py:71](../../../waifu2x/reconstruct.py#L71)

#### Signature

```python
def get_tta_patterns(src: np.ndarray, n: int):
    ...
```



## image

[Show source in reconstruct.py:127](../../../waifu2x/reconstruct.py#L127)

#### Signature

```python
def image(src, model, block_size: int, batch_size: int) -> Image.Image:
    ...
```



## image_tta

[Show source in reconstruct.py:92](../../../waifu2x/reconstruct.py#L92)

#### Signature

```python
def image_tta(
    src: Image.Image,
    model: chainer.Chain,
    tta_level: int,
    block_size: int,
    batch_size: int,
):
    ...
```



## inv

[Show source in reconstruct.py:65](../../../waifu2x/reconstruct.py#L65)

#### Signature

```python
def inv(rot: int, flip: bool = False):
    ...
```


