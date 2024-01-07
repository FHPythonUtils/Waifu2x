# Srcnn

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Srcnn

> Auto-generated documentation for [waifu2x.srcnn](../../../waifu2x/srcnn.py) module.

- [Srcnn](#srcnn)
  - [ResBlock](#resblock)
  - [ResNet10](#resnet10)
  - [UpConv7](#upconv7)
  - [UpResNet10](#upresnet10)
  - [VGG7](#vgg7)

## ResBlock

[Show source in srcnn.py:62](../../../waifu2x/srcnn.py#L62)

#### Signature

```python
class ResBlock(chainer.Chain):
    def __init__(
        self,
        in_channels,
        out_channels,
        slope: float = 0.1,
        r: int = 16,
        se: bool = False,
    ): ...
```



## ResNet10

[Show source in srcnn.py:98](../../../waifu2x/srcnn.py#L98)

#### Signature

```python
class ResNet10(chainer.Chain):
    def __init__(self, ch): ...
```



## UpConv7

[Show source in srcnn.py:35](../../../waifu2x/srcnn.py#L35)

#### Signature

```python
class UpConv7(chainer.Chain):
    def __init__(self, ch: int): ...
```



## UpResNet10

[Show source in srcnn.py:128](../../../waifu2x/srcnn.py#L128)

#### Signature

```python
class UpResNet10(chainer.Chain):
    def __init__(self, ch): ...
```



## VGG7

[Show source in srcnn.py:8](../../../waifu2x/srcnn.py#L8)

#### Signature

```python
class VGG7(chainer.Chain):
    def __init__(self, ch): ...
```