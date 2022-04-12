# Srcnn

> Auto-generated documentation for [waifu2x.srcnn](../../../waifu2x/srcnn.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../MODULES.md#waifu2x-modules) / [Waifu2x](index.md#waifu2x) / Srcnn
    - [ResBlock](#resblock)
    - [ResNet10](#resnet10)
    - [UpConv7](#upconv7)
    - [UpResNet10](#upresnet10)
    - [VGG7](#vgg7)

## ResBlock

[[find in source code]](../../../waifu2x/srcnn.py#L62)

```python
class ResBlock(chainer.Chain):
    def __init__(
        in_channels,
        out_channels,
        slope: float = 0.1,
        r: int = 16,
        se: bool = False,
    ):
```

## ResNet10

[[find in source code]](../../../waifu2x/srcnn.py#L98)

```python
class ResNet10(chainer.Chain):
    def __init__(ch):
```

## UpConv7

[[find in source code]](../../../waifu2x/srcnn.py#L35)

```python
class UpConv7(chainer.Chain):
    def __init__(ch: int):
```

## UpResNet10

[[find in source code]](../../../waifu2x/srcnn.py#L128)

```python
class UpResNet10(chainer.Chain):
    def __init__(ch):
```

## VGG7

[[find in source code]](../../../waifu2x/srcnn.py#L8)

```python
class VGG7(chainer.Chain):
    def __init__(ch):
```
