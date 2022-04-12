# Data Augmentation

> Auto-generated documentation for [waifu2x.data_augmentation](../../../waifu2x/data_augmentation.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../MODULES.md#waifu2x-modules) / [Waifu2x](index.md#waifu2x) / Data Augmentation
    - [color_noise](#color_noise)
    - [flip](#flip)
    - [half](#half)
    - [shift_1px](#shift_1px)
    - [unsharp_mask](#unsharp_mask)

## color_noise

[[find in source code]](../../../waifu2x/data_augmentation.py#L22)

```python
def color_noise(src: np.ndarray, p, factor: float = 0.1) -> np.ndarray:
```

## flip

[[find in source code]](../../../waifu2x/data_augmentation.py#L33)

```python
def flip(src: np.ndarray) -> np.ndarray:
```

## half

[[find in source code]](../../../waifu2x/data_augmentation.py#L45)

```python
def half(src: np.ndarray, p: np.ndarray) -> np.ndarray:
```

## shift_1px

[[find in source code]](../../../waifu2x/data_augmentation.py#L54)

```python
def shift_1px(src: np.ndarray) -> np.ndarray:
```

## unsharp_mask

[[find in source code]](../../../waifu2x/data_augmentation.py#L11)

```python
def unsharp_mask(src: np.ndarray, p) -> np.ndarray:
```
