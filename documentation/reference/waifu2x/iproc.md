# Iproc

[Waifu2x Index](../README.md#waifu2x-index) / [Waifu2x](./index.md#waifu2x) / Iproc

> Auto-generated documentation for [waifu2x.iproc](../../../waifu2x/iproc.py) module.

- [Iproc](#iproc)
  - [alpha_make_border](#alpha_make_border)
  - [array_to_wand](#array_to_wand)
  - [clipped_psnr](#clipped_psnr)
  - [jpeg](#jpeg)
  - [nn_scaling](#nn_scaling)
  - [pcacov](#pcacov)
  - [read_image_rgb_uint8](#read_image_rgb_uint8)
  - [wand_to_array](#wand_to_array)

## alpha_make_border

[Show source in iproc.py:23](../../../waifu2x/iproc.py#L23)

#### Signature

```python
def alpha_make_border(rgb: np.ndarray, alpha: np.ndarray | None, model: Chain): ...
```



## array_to_wand

[Show source in iproc.py:73](../../../waifu2x/iproc.py#L73)

Convert image (nd.array) to wand.image.Image.

#### Signature

```python
def array_to_wand(src: np.ndarray): ...
```



## clipped_psnr

[Show source in iproc.py:124](../../../waifu2x/iproc.py#L124)

#### Signature

```python
def clipped_psnr(y, t, a_min: float = 0.0, a_max: float = 1.0): ...
```



## jpeg

[Show source in iproc.py:111](../../../waifu2x/iproc.py#L111)

#### Signature

```python
def jpeg(src, sampling_factor: str = "1x1,1x1,1x1", quality: int = 90): ...
```



## nn_scaling

[Show source in iproc.py:91](../../../waifu2x/iproc.py#L91)

#### Signature

```python
def nn_scaling(
    src: Image.Image | np.ndarray | None, ratio: float
) -> Image.Image | np.ndarray | None: ...
```



## pcacov

[Show source in iproc.py:118](../../../waifu2x/iproc.py#L118)

#### Signature

```python
def pcacov(x: np.ndarray): ...
```



## read_image_rgb_uint8

[Show source in iproc.py:53](../../../waifu2x/iproc.py#L53)

Read an image from a path as a numpy uint8 array.

#### Arguments

- `path` *str* - path of the image to open

#### Returns

Type: *np.ndarray*
image as numpy uint8 array

#### Signature

```python
def read_image_rgb_uint8(path: str) -> np.ndarray: ...
```



## wand_to_array

[Show source in iproc.py:83](../../../waifu2x/iproc.py#L83)

Convert image (wand.image.Image) to nd.array.

#### Signature

```python
def wand_to_array(src: wand.image.Image): ...
```