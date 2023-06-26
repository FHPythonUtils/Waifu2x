<!-- omit in toc -->
# Python Module Tutorial

- [Step 1](#step-1)
- [Step 2](#step-2)
- [Step 3](#step-3)

## Step 1

Organise images into a single directory eg `images/`

For example, the following files:

<div>
<img src="../../tests/data/background.png" alt="Screenshot 1" width="300">
<img src="../../tests/data/foreground.png" alt="Screenshot 2" width="300">
</div>

## Step 2

```python
from waifu2x import run

input_img_path = "foreground.png"
output_img_path = "foreground_actual.png"
run(input_img_path,output_img_path)
```

## Step 3

Output can be found in `output_images/`

For example, the following files:

<div>
<img src="../../tests/data/background_expected.png" alt="Screenshot 1" width="300">
<img src="../../tests/data/foreground_expected.png" alt="Screenshot 2" width="300">
</div>
