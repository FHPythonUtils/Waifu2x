# srcnn

> Auto-generated documentation for [waifu2x.srcnn](../../waifu2x/srcnn.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / srcnn
    - [ResBlock](#resblock)
    - [ResNet10](#resnet10)
    - [UpConv7](#upconv7)
    - [UpResNet10](#upresnet10)
    - [VGG7](#vgg7)

## ResBlock

[[find in source code]](../../waifu2x/srcnn.py#L60)

```python
class ResBlock(chainer.Chain):
    def __init__(in_channels, out_channels, slope=0.1, r=16, se=False):
```

## ResNet10

[[find in source code]](../../waifu2x/srcnn.py#L94)

```python
class ResNet10(chainer.Chain):
    def __init__(ch):
```

## UpConv7

[[find in source code]](../../waifu2x/srcnn.py#L33)

```python
class UpConv7(chainer.Chain):
    def __init__(ch):
```

## UpResNet10

[[find in source code]](../../waifu2x/srcnn.py#L124)

```python
class UpResNet10(chainer.Chain):
    def __init__(ch):
```

## VGG7

[[find in source code]](../../waifu2x/srcnn.py#L6)

```python
class VGG7(chainer.Chain):
    def __init__(ch):
```
