# Waifu2x

[Waifu2x Index](../README.md#waifu2x-index) / Waifu2x

> Auto-generated documentation for [waifu2x](../../../waifu2x/__init__.py) module.

- [Waifu2x](#waifu2x)
  - [denoise_image](#denoise_image)
  - [load_models](#load_models)
  - [main](#main)
  - [run](#run)
  - [split_alpha](#split_alpha)
  - [upscale_image](#upscale_image)
  - [Modules](#modules)

## denoise_image

[Show source in __init__.py:32](../../../waifu2x/__init__.py#L32)

Remove noise from an image (src) using a scale model and an alpha model.

#### Arguments

----
 - `args` *argparse.Namespace* - argparse namespace containing config such as the block_size
 - `src` *Image.Image* - Pillow image to remove noise from
 - `model` *Chain* - model for scaling
 - `should_print` *bool* - Flag to enable print to console

#### Returns

-------
 - `Image.Image` - Pillow image with noise removed

#### Signature

```python
def denoise_image(
    args: argparse.Namespace, src: Image.Image, model: Chain, should_print: bool = True
) -> Image.Image: ...
```



## load_models

[Show source in __init__.py:157](../../../waifu2x/__init__.py#L157)

Load models using a args config.

#### Arguments

----
 - `args` *argparse.Namespace* - argparse namespace containing config such as the arch and color

#### Returns

-------
 - `dict[str,` *Chain]* - Mapping of model names to Chain models

#### Signature

```python
def load_models(args: argparse.Namespace) -> dict[str, Chain]: ...
```



## main

[Show source in __init__.py:27](../../../waifu2x/__init__.py#L27)

Run the program, from the main entry point.

#### Signature

```python
def main() -> None: ...
```



## run

[Show source in __init__.py:211](../../../waifu2x/__init__.py#L211)

Run waifu2x using mostly the same inputs as CLI ones.

#### Arguments

- `input_img_path` *str* - Input image/ directory, defaults to "images/small.png"
- `output_img_path` *str* - Directory to write output images to, defaults to "./"
- `gpu` *int* - CUDA enabled GPU to use, defaults to -1
:param int | None quality: Set the quality of output images 1-100 (None=100), defaults to None
:param str | None model_dir: Specify a custom directory containing models, defaults to None
- `scale_ratio` *float* - Specify a scale, defaults to 2.0
- `batch_size` *int* - _description_, defaults to 16
- `block_size` *int* - _description_, defaults to 128
- `extension` *str* - Select output extension png/webp
- `arch` *str* - _description_, defaults to "VGG7"
- `method` *str* - _description_, defaults to "scale"
- `noise_level` *int* - _description_, defaults to 1
- `color` *str* - _description_, defaults to "rgb"
- `tta_level` *int* - _description_, defaults to 8
- `width` *int* - _description_, defaults to 0
- `height` *int* - _description_, defaults to 0
- `shorter_side` *int* - _description_, defaults to 0
- `longer_side` *int* - _description_, defaults to 0
- `should_print` *bool* - _description_, defaults to True

#### Raises

- `ValueError` -  Output file extension not supported

#### Signature

```python
def run(
    input_img_path: str = "images/small.png",
    output_img_path: str = "./",
    gpu: int = -1,
    quality: int | None = None,
    model_dir: str | None = None,
    scale_ratio: float = 2.0,
    batch_size: int = 16,
    block_size: int = 128,
    extension: str = "png",
    arch: str = "VGG7",
    method: str = "scale",
    noise_level: int = 1,
    color: str = "rgb",
    tta_level: int = 8,
    width: int = 0,
    height: int = 0,
    shorter_side: int = 0,
    longer_side: int = 0,
    should_print: bool = True,
) -> None: ...
```



## split_alpha

[Show source in __init__.py:128](../../../waifu2x/__init__.py#L128)

Split the image into an rgb, and alpha tuple.

:param Image.Image src: image

#### Arguments

- `model` *Chain* - model to use
- `should_print` *bool* - print to stdout?, defaults to True

#### Returns

Type: *tuple[Image.Image, Image.Image | None]*
rgb, and alpha tuple

#### Signature

```python
def split_alpha(
    src: Image.Image, model: Chain, should_print: bool = True
) -> tuple[Image.Image, Image.Image | None]: ...
```



## upscale_image

[Show source in __init__.py:69](../../../waifu2x/__init__.py#L69)

Upscale an image (src) using a scale model and an alpha model.

#### Arguments

----
 - `args` *argparse.Namespace* - argparse namespace containing config such as the scale_ratio and
 block size
 - `src` *Image.Image* - Pillow image to upscale
 - `scale_model` *Chain* - model to use for scaling
 - `alpha_model` *Chain, optional* - model to use for alpha. Defaults to None.
 - `should_print` *bool* - flag to enable output to console

#### Returns

-------
 - `Image.Image` - upscaled Pillow image

#### Signature

```python
def upscale_image(
    args: argparse.Namespace,
    src: Image.Image,
    scale_model: Chain,
    alpha_model: Chain | None = None,
    should_print: bool = True,
) -> Image.Image: ...
```



## Modules

- [Module](./module.md)
- [Data Augmentation](./data_augmentation.md)
- [DatasetSampler](./dataset_sampler.md)
- [Iproc](./iproc.md)
- [Loss](loss/index.md)
- [Pairwise Transform](./pairwise_transform.md)
- [Reconstruct](./reconstruct.md)
- [Srcnn](./srcnn.md)
- [Utils](./utils.md)