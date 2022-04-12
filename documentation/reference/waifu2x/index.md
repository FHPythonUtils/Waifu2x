# Waifu2x

> Auto-generated documentation for [waifu2x](../../../waifu2x/__init__.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../MODULES.md#waifu2x-modules) / Waifu2x
    - [denoise_image](#denoise_image)
    - [load_models](#load_models)
    - [main](#main)
    - [split_alpha](#split_alpha)
    - [upscale_image](#upscale_image)
    - Modules
        - [Module](module.md#module)
        - [Data Augmentation](data_augmentation.md#data-augmentation)
        - [DatasetSampler](dataset_sampler.md#datasetsampler)
        - [Iproc](iproc.md#iproc)
        - [Loss](loss/index.md#loss)
        - [Pairwise Transform](pairwise_transform.md#pairwise-transform)
        - [Reconstruct](reconstruct.md#reconstruct)
        - [Srcnn](srcnn.md#srcnn)
        - [Utils](utils.md#utils)

## denoise_image

[[find in source code]](../../../waifu2x/__init__.py#L20)

```python
def denoise_image(
    args: argparse.Namespace,
    src: Image.Image,
    model: chainer.Chain,
) -> Image.Image:
```

Remove noise from an image (src) using a scale model and an alpha model

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the block_size
- `src` *Image.Image* - Pillow image to remove noise from
- `scale_model` *chainer.Chain* - model to use for scaling

#### Returns

- `Image.Image` - Pillow image with noise removed

## load_models

[[find in source code]](../../../waifu2x/__init__.py#L110)

```python
def load_models(args: argparse.Namespace) -> dict[str, chainer.Chain]:
```

Load models using a args config

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the arch and color

#### Returns

- `dict[str,` *chainer.Chain]* - Mapping of model names to chainer.Chain models

## main

[[find in source code]](../../../waifu2x/__init__.py#L161)

```python
def main():
```

Main entry point to the program

#### Raises

- `ValueError` - Output file extension not supported

## split_alpha

[[find in source code]](../../../waifu2x/__init__.py#L93)

```python
def split_alpha(
    src: Image.Image,
    model: chainer.Chain,
) -> tuple[Image.Image, Image.Image | None]:
```

## upscale_image

[[find in source code]](../../../waifu2x/__init__.py#L45)

```python
def upscale_image(
    args: argparse.Namespace,
    src: Image.Image,
    scale_model: chainer.Chain,
    alpha_model: chainer.Chain | None = None,
) -> Image.Image:
```

Upscale an image (src) using a scale model and an alpha model

#### Arguments

- `args` *argparse.Namespace* - argparse namespace containing config such as the scale_ratio and block size
- `src` *Image.Image* - Pillow image to upscale
- `scale_model` *chainer.Chain* - model to use for scaling
- `alpha_model` *chainer.Chain, optional* - model to use for alpha. Defaults to None.

#### Returns

- `Image.Image` - upscaled Pillow image
