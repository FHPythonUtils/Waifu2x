# clipped_weighted_huber_loss

> Auto-generated documentation for [waifu2x.loss.clipped_weighted_huber_loss](../../../waifu2x/loss/clipped_weighted_huber_loss.py) module.

- [Waifu2x](../../README.md#waifu2x-index) / [Modules](../../README.md#waifu2x-modules) / [waifu2x](../index.md#waifu2x) / [loss](index.md#loss) / clipped_weighted_huber_loss
    - [ClippedWeightedHuberLoss](#clippedweightedhuberloss)
        - [ClippedWeightedHuberLoss().backward](#clippedweightedhuberlossbackward)
        - [ClippedWeightedHuberLoss().check_type_forward](#clippedweightedhuberlosscheck_type_forward)
        - [ClippedWeightedHuberLoss().forward](#clippedweightedhuberlossforward)
    - [clipped_weighted_huber_loss](#clipped_weighted_huber_loss)

## ClippedWeightedHuberLoss

[[find in source code]](../../../waifu2x/loss/clipped_weighted_huber_loss.py#L6)

```python
class ClippedWeightedHuberLoss(function.Function):
    def __init__(weight, delta=0.1, clip=(0.0, 1.0)):
```

### ClippedWeightedHuberLoss().backward

[[find in source code]](../../../waifu2x/loss/clipped_weighted_huber_loss.py#L36)

```python
def backward(inputs, grad_outputs):
```

### ClippedWeightedHuberLoss().check_type_forward

[[find in source code]](../../../waifu2x/loss/clipped_weighted_huber_loss.py#L12)

```python
def check_type_forward(in_types):
```

### ClippedWeightedHuberLoss().forward

[[find in source code]](../../../waifu2x/loss/clipped_weighted_huber_loss.py#L20)

```python
def forward(inputs):
```

## clipped_weighted_huber_loss

[[find in source code]](../../../waifu2x/loss/clipped_weighted_huber_loss.py#L45)

```python
def clipped_weighted_huber_loss(x, t, weight, delta=0.1, clip=(0.0, 1.0)):
```
