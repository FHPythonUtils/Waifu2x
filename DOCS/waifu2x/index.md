# waifu2x

> Auto-generated documentation for [waifu2x](../../waifu2x/__init__.py) module.

- [Waifu2x](../README.md#waifu2x-index) / [Modules](../README.md#waifu2x-modules) / waifu2x
    - [denoise_image](#denoise_image)
    - [load_models](#load_models)
    - [main](#main)
    - [split_alpha](#split_alpha)
    - [upscale_image](#upscale_image)
    - Modules
        - [\_\_main\_\_](module.md#__main__)
        - [data_augmentation](data_augmentation.md#data_augmentation)
        - [dataset_sampler](dataset_sampler.md#dataset_sampler)
        - [iproc](iproc.md#iproc)
        - [loss](loss/index.md#loss)
        - [pairwise_transform](pairwise_transform.md#pairwise_transform)
        - [reconstruct](reconstruct.md#reconstruct)
        - [srcnn](srcnn.md#srcnn)
        - [utils](utils.md#utils)

## denoise_image

[[find in source code]](../../waifu2x/__init__.py#L19)

```python
def denoise_image(
    args: argparse.Namespace,
    src: Image.Image,
    model,
) -> Image.Image:
```

## load_models

[[find in source code]](../../waifu2x/__init__.py#L85)

```python
def load_models(args: argparse.Namespace):
```

## main

[[find in source code]](../../waifu2x/__init__.py#L128)

```python
def main():
```

## split_alpha

[[find in source code]](../../waifu2x/__init__.py#L68)

```python
def split_alpha(
    src: Image.Image,
    model,
) -> tuple[(Image.Image, Image.Image | None)]:
```

## upscale_image

[[find in source code]](../../waifu2x/__init__.py#L34)

```python
def upscale_image(
    args: argparse.Namespace,
    src: Image.Image,
    scale_model,
    alpha_model=None,
) -> Image.Image:
```
