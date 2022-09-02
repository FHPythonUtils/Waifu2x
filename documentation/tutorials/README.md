
#

- [Step 1](#step-1)
- [Step 2](#step-2)
- [Step 3](#step-3)

## Step 1

Organise images into a single directory eg 'images/'

## Step 2

Run 'waifu2x' as follows:

```sh
poetry run py -m waifu2x -i images -o output_images
```

See below for a breakdown

- `poetry run`: in this example we are using poetry to run the python code inside a virtual environment. This is optional but good practise
- `py -m waifu2x`: tell python to use waifu2x module (this library). If on Mac/ Linux use `python3 -m waifu2x`
- `-i images`: the input directory of images
- `-o output_images`: the output directory

## Step 3

Output can be found in 'output_images/'
