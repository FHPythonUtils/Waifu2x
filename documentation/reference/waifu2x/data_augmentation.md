# Data Augmentation

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Data Augmentation

> Auto-generated documentation for [waifu2x.data_augmentation](../../../waifu2x/data_augmentation.py) module.

- [Data Augmentation](#data-augmentation)
  - [color_noise](#color_noise)
  - [flip](#flip)
  - [half](#half)
  - [shift_1px](#shift_1px)
  - [unsharp_mask](#unsharp_mask)

## color_noise

[Show source in data_augmentation.py:22](../../../waifu2x/data_augmentation.py#L22)

#### Signature

```python
def color_noise(src: np.ndarray, p, factor: float = 0.1) -> np.ndarray: ...
```



## flip

[Show source in data_augmentation.py:33](../../../waifu2x/data_augmentation.py#L33)

#### Signature

```python
def flip(src: np.ndarray) -> np.ndarray: ...
```



## half

[Show source in data_augmentation.py:45](../../../waifu2x/data_augmentation.py#L45)

#### Signature

```python
def half(src: np.ndarray, p: np.ndarray) -> np.ndarray: ...
```



## shift_1px

[Show source in data_augmentation.py:54](../../../waifu2x/data_augmentation.py#L54)

#### Signature

```python
def shift_1px(src: np.ndarray) -> np.ndarray: ...
```



## unsharp_mask

[Show source in data_augmentation.py:11](../../../waifu2x/data_augmentation.py#L11)

#### Signature

```python
def unsharp_mask(src: np.ndarray, p) -> np.ndarray: ...
```