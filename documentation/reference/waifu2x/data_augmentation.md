# Data Augmentation

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Data Augmentation

> Auto-generated documentation for [waifu2x.data_augmentation](../../../waifu2x/data_augmentation.py) module.

- [Data Augmentation](#data-augmentation)
  - [color_noise](#color_noise)
  - [flip](#flip)
  - [half](#half)
  - [shift_1px](#shift_1px)
  - [unsharp_mask](#unsharp_mask)

## color_noise

[Show source in data_augmentation.py:48](../../../waifu2x/data_augmentation.py#L48)

Apply color noise to the input image array.

#### Arguments

----
- `src` *np.ndarray* - Input image array.
- `p` *float* - Probability of applying the noise.
- `factor` *float* - Noise factor.

#### Returns

-------
- `np.ndarray` - Processed image array.

#### Signature

```python
def color_noise(src: np.ndarray, p: float, factor: float = 0.1) -> np.ndarray: ...
```



## flip

[Show source in data_augmentation.py:73](../../../waifu2x/data_augmentation.py#L73)

Flip the input image array.

#### Arguments

----
- `src` *np.ndarray* - Input image array.

#### Returns

-------
- `np.ndarray` - Processed image array.

#### Signature

```python
def flip(src: np.ndarray) -> np.ndarray: ...
```



## half

[Show source in data_augmentation.py:97](../../../waifu2x/data_augmentation.py#L97)

Scale down the input image array by half.

#### Arguments

----
- `src` *np.ndarray* - Input image array.
- `p` *np.ndarray* - Probability array.

#### Returns

-------
- `np.ndarray` - Processed image array.

#### Signature

```python
def half(src: np.ndarray, p: np.ndarray) -> np.ndarray: ...
```



## shift_1px

[Show source in data_augmentation.py:117](../../../waifu2x/data_augmentation.py#L117)

Shift the input image array by 1 pixel.

#### Arguments

----
- src (np.ndarray): Input image array.

#### Returns

-------
- `-` *np.ndarray* - Shifted image array.

#### Signature

```python
def shift_1px(src: np.ndarray) -> np.ndarray: ...
```



## unsharp_mask

[Show source in data_augmentation.py:26](../../../waifu2x/data_augmentation.py#L26)

Apply unsharp mask filter to the input image array.

#### Arguments

----
- `src` *np.ndarray* - Input image array.
- `p` *float* - Probability of applying the filter.

#### Returns

-------
- `np.ndarray` - Processed image array.

#### Signature

```python
def unsharp_mask(src: np.ndarray, p: float) -> np.ndarray: ...
```