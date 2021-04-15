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

[[find in source code]](../../waifu2x/__init__.py#L15)

```python
def denoise_image(cfg, src, model):
```

## load_models

[[find in source code]](../../waifu2x/__init__.py#L74)

```python
def load_models(cfg):
```

## main

[[find in source code]](../../waifu2x/__init__.py#L117)

```python
def main():
```

## split_alpha

[[find in source code]](../../waifu2x/__init__.py#L60)

```python
def split_alpha(src, model):
```

## upscale_image

[[find in source code]](../../waifu2x/__init__.py#L30)

```python
def upscale_image(cfg, src, scale_model, alpha_model=None):
```
