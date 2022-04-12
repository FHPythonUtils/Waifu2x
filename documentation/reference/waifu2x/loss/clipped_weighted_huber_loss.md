# ClippedWeightedHuberLoss

> Auto-generated documentation for [waifu2x.loss.clipped_weighted_huber_loss](../../../../waifu2x/loss/clipped_weighted_huber_loss.py) module.

- [Waifu2x](../../README.md#waifu2x-index) / [Modules](../../MODULES.md#waifu2x-modules) / [Waifu2x](../index.md#waifu2x) / [Loss](index.md#loss) / ClippedWeightedHuberLoss
    - [ClippedWeightedHuberLoss](#clippedweightedhuberloss)
        - [ClippedWeightedHuberLoss().backward](#clippedweightedhuberlossbackward)
        - [ClippedWeightedHuberLoss().check_type_forward](#clippedweightedhuberlosscheck_type_forward)
        - [ClippedWeightedHuberLoss().forward](#clippedweightedhuberlossforward)
    - [clipped_weighted_huber_loss](#clipped_weighted_huber_loss)

## ClippedWeightedHuberLoss

[[find in source code]](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L8)

```python
class ClippedWeightedHuberLoss(function.Function):
    def __init__(
        weight,
        delta: float = 0.1,
        clip: tuple[float, float] = (0.0, 1.0),
    ):
```

### ClippedWeightedHuberLoss().backward

[[find in source code]](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L40)

```python
def backward(inputs, grad_outputs):
```

### ClippedWeightedHuberLoss().check_type_forward

[[find in source code]](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L15)

```python
def check_type_forward(in_types):
```

### ClippedWeightedHuberLoss().forward

[[find in source code]](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L24)

```python
def forward(inputs):
```

## clipped_weighted_huber_loss

[[find in source code]](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L49)

```python
def clipped_weighted_huber_loss(
    x,
    t,
    weight,
    delta: float = 0.1,
    clip: tuple[float, float] = (0.0, 1.0),
):
```
