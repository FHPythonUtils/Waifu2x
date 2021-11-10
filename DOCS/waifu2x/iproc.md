# iproc

> Auto-generated documentation for [waifu2x.iproc](../../waifu2x/iproc.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / [waifu2x](index.md#waifu2x) / iproc
    - [alpha_make_border](#alpha_make_border)
    - [array_to_wand](#array_to_wand)
    - [clipped_psnr](#clipped_psnr)
    - [jpeg](#jpeg)
    - [nn_scaling](#nn_scaling)
    - [pcacov](#pcacov)
    - [read_image_rgb_uint8](#read_image_rgb_uint8)
    - [wand_to_array](#wand_to_array)

## alpha_make_border

[[find in source code]](../../waifu2x/iproc.py#L16)

```python
def alpha_make_border(rgb: Image.Image, alpha: Image.Image | None, model):
```

## array_to_wand

[[find in source code]](../../waifu2x/iproc.py#L63)

```python
def array_to_wand(src: np.ndarray):
```

## clipped_psnr

[[find in source code]](../../waifu2x/iproc.py#L110)

```python
def clipped_psnr(y, t, a_min: float = 0.0, a_max: float = 1.0):
```

## jpeg

[[find in source code]](../../waifu2x/iproc.py#L97)

```python
def jpeg(src, sampling_factor: str = '1x1,1x1,1x1', quality: int = 90):
```

## nn_scaling

[[find in source code]](../../waifu2x/iproc.py#L80)

```python
def nn_scaling(
    src: Image.Image | np.ndarray | None,
    ratio: int,
) -> Image.Image | np.ndarray | None:
```

## pcacov

[[find in source code]](../../waifu2x/iproc.py#L104)

```python
def pcacov(x):
```

## read_image_rgb_uint8

[[find in source code]](../../waifu2x/iproc.py#L46)

```python
def read_image_rgb_uint8(path: str):
```

## wand_to_array

[[find in source code]](../../waifu2x/iproc.py#L72)

```python
def wand_to_array(src: wand.image.Image):
```
