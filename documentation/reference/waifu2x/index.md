# Waifu2x

[Waifu2x Index](../README.md#waifu2x-index) /
Waifu2x

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

[Show source in __init__.py:25](../../../waifu2x/__init__.py#L25)

Remove noise from an image (src) using a scale model and an alpha model

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the block_size
- `src` *Image.Image* - Pillow image to remove noise from
- `scale_model` *chainer.Chain* - model to use for scaling

#### Returns

- `Image.Image` - Pillow image with noise removed

#### Signature

```python
def denoise_image(
    args: argparse.Namespace,
    src: Image.Image,
    model: chainer.Chain,
    should_print: bool = True,
) -> Image.Image: ...
```



## load_models

[Show source in __init__.py:129](../../../waifu2x/__init__.py#L129)

Load models using a args config

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the arch and color

#### Returns

- `dict[str,` *chainer.Chain]* - Mapping of model names to chainer.Chain models

#### Signature

```python
def load_models(args: argparse.Namespace) -> dict[str, chainer.Chain]: ...
```



## main

[Show source in __init__.py:20](../../../waifu2x/__init__.py#L20)

Main entry point to the program.

#### Signature

```python
def main(): ...
```



## run

[Show source in __init__.py:180](../../../waifu2x/__init__.py#L180)

Runs waifu2x. Mostly the same inputs as CLI ones.

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
): ...
```



## split_alpha

[Show source in __init__.py:107](../../../waifu2x/__init__.py#L107)

#### Signature

```python
def split_alpha(
    src: Image.Image, model: chainer.Chain, should_print: bool = True
) -> tuple[Image.Image, Image.Image | None]: ...
```



## upscale_image

[Show source in __init__.py:54](../../../waifu2x/__init__.py#L54)

Upscale an image (src) using a scale model and an alpha model

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the scale_ratio and block size
- `src` *Image.Image* - Pillow image to upscale
- `scale_model` *chainer.Chain* - model to use for scaling
- `alpha_model` *chainer.Chain, optional* - model to use for alpha. Defaults to None.

#### Returns

- `Image.Image` - upscaled Pillow image

#### Signature

```python
def upscale_image(
    args: argparse.Namespace,
    src: Image.Image,
    scale_model: chainer.Chain,
    alpha_model: chainer.Chain | None = None,
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