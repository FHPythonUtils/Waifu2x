# Srcnn

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Srcnn

> Auto-generated documentation for [waifu2x.srcnn](../../../waifu2x/srcnn.py) module.

- [Srcnn](#srcnn)
  - [ResBlock](#resblock)
  - [ResNet10](#resnet10)
  - [UpConv7](#upconv7)
  - [UpResNet10](#upresnet10)
  - [VGG7](#vgg7)

## ResBlock

[Show source in srcnn.py:60](../../../waifu2x/srcnn.py#L60)

#### Signature

```python
class ResBlock(Chain):
    def __init__(
        self,
        in_channels,
        out_channels,
        slope: float = 0.1,
        r: int = 16,
        se: bool = False,
    ) -> None: ...
```



## ResNet10

[Show source in srcnn.py:96](../../../waifu2x/srcnn.py#L96)

#### Signature

```python
class ResNet10(Chain):
    def __init__(self, ch) -> None: ...
```



## UpConv7

[Show source in srcnn.py:34](../../../waifu2x/srcnn.py#L34)

#### Signature

```python
class UpConv7(Chain):
    def __init__(self, ch: int) -> None: ...
```



## UpResNet10

[Show source in srcnn.py:125](../../../waifu2x/srcnn.py#L125)

#### Signature

```python
class UpResNet10(Chain):
    def __init__(self, ch) -> None: ...
```



## VGG7

[Show source in srcnn.py:8](../../../waifu2x/srcnn.py#L8)

#### Signature

```python
class VGG7(Chain):
    def __init__(self, ch) -> None: ...
```