# Iproc

[Waifu2x Index](../README.md#waifu2x-index) /
[Waifu2x](./index.md#waifu2x) /
Iproc

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

[Show source in iproc.py:17](../../../waifu2x/iproc.py#L17)

#### Signature

```python
def alpha_make_border(rgb: np.ndarray, alpha: np.ndarray | None, model: chainer.Chain):
    ...
```



## array_to_wand

[Show source in iproc.py:64](../../../waifu2x/iproc.py#L64)

#### Signature

```python
def array_to_wand(src: np.ndarray):
    ...
```



## clipped_psnr

[Show source in iproc.py:111](../../../waifu2x/iproc.py#L111)

#### Signature

```python
def clipped_psnr(y, t, a_min: float = 0.0, a_max: float = 1.0):
    ...
```



## jpeg

[Show source in iproc.py:98](../../../waifu2x/iproc.py#L98)

#### Signature

```python
def jpeg(src, sampling_factor: str = "1x1,1x1,1x1", quality: int = 90):
    ...
```



## nn_scaling

[Show source in iproc.py:81](../../../waifu2x/iproc.py#L81)

#### Signature

```python
def nn_scaling(
    src: Image.Image | np.ndarray | None, ratio: int
) -> Image.Image | np.ndarray | None:
    ...
```



## pcacov

[Show source in iproc.py:105](../../../waifu2x/iproc.py#L105)

#### Signature

```python
def pcacov(x: np.ndarray):
    ...
```



## read_image_rgb_uint8

[Show source in iproc.py:47](../../../waifu2x/iproc.py#L47)

#### Signature

```python
def read_image_rgb_uint8(path: str):
    ...
```



## wand_to_array

[Show source in iproc.py:73](../../../waifu2x/iproc.py#L73)

#### Signature

```python
def wand_to_array(src: wand.image.Image):
    ...
```


