# ClippedWeightedHuberLoss

[Waifu2x Index](../../README.md#waifu2x-index) /
[Waifu2x](../index.md#waifu2x) /
[Loss](./index.md#loss) /
ClippedWeightedHuberLoss

> Auto-generated documentation for [waifu2x.loss.clipped_weighted_huber_loss](../../../../waifu2x/loss/clipped_weighted_huber_loss.py) module.

- [ClippedWeightedHuberLoss](#clippedweightedhuberloss)
  - [ClippedWeightedHuberLoss](#clippedweightedhuberloss-1)
    - [ClippedWeightedHuberLoss().backward](#clippedweightedhuberloss()backward)
    - [ClippedWeightedHuberLoss().check_type_forward](#clippedweightedhuberloss()check_type_forward)
    - [ClippedWeightedHuberLoss().forward](#clippedweightedhuberloss()forward)
  - [clipped_weighted_huber_loss](#clipped_weighted_huber_loss)

## ClippedWeightedHuberLoss

[Show source in clipped_weighted_huber_loss.py:8](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L8)

#### Signature

```python
class ClippedWeightedHuberLoss(function.Function):
    def __init__(
        self, weight, delta: float = 0.1, clip: tuple[float, float] = (0.0, 1.0)
    ): ...
```

### ClippedWeightedHuberLoss().backward

[Show source in clipped_weighted_huber_loss.py:40](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L40)

#### Signature

```python
def backward(self, inputs, grad_outputs): ...
```

### ClippedWeightedHuberLoss().check_type_forward

[Show source in clipped_weighted_huber_loss.py:15](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L15)

#### Signature

```python
def check_type_forward(self, in_types): ...
```

### ClippedWeightedHuberLoss().forward

[Show source in clipped_weighted_huber_loss.py:24](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L24)

#### Signature

```python
def forward(self, inputs): ...
```



## clipped_weighted_huber_loss

[Show source in clipped_weighted_huber_loss.py:49](../../../../waifu2x/loss/clipped_weighted_huber_loss.py#L49)

#### Signature

```python
def clipped_weighted_huber_loss(
    x, t, weight, delta: float = 0.1, clip: tuple[float, float] = (0.0, 1.0)
): ...
```