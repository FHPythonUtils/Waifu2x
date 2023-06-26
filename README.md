[![GitHub top language](https://img.shields.io/github/languages/top/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](../../)
[![Repository size](https://img.shields.io/github/repo-size/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](../../)
[![Issues](https://img.shields.io/github/issues/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](../../issues)
[![License](https://img.shields.io/github/license/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](/LICENSE.md)
[![Commit activity](https://img.shields.io/github/commit-activity/m/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/FHPythonUtils/Waifu2x.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/waifu2x.svg?style=for-the-badge)](https://pypistats.org/packages/waifu2x)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fwaifu2x)](https://pepy.tech/project/waifu2x)
[![PyPI Version](https://img.shields.io/pypi/v/waifu2x.svg?style=for-the-badge)](https://pypi.org/project/waifu2x)

<!-- omit in toc -->
# Waifu2x

<img src="readme-assets/icons/name.png" alt="Project Icon" width="750">

Chainer implementation of waifu2x.

## Help

```raw
usage: __main__.py [-h] [--gpu GPU] [--input INPUT] [--output OUTPUT]
                   [--quality QUALITY] [--model_dir MODEL_DIR]
                   [--scale_ratio SCALE_RATIO] [--tta]
                   [--batch_size BATCH_SIZE] [--block_size BLOCK_SIZE]
                   [--extension {png,webp}]
                   [--arch {VGG7,0,UpConv7,1,ResNet10,2,UpResNet10,3}]
                   [--method {noise,scale,noise_scale}]
                   [--noise_level {0,1,2,3}] [--color {y,rgb}]
                   [--tta_level {2,4,8}]
                   [--width WIDTH | --height HEIGHT | --shorter_side SHORTER_SIDE | --longer_side LONGER_SIDE]

Chainer implementation of waifu2x

optional arguments:
  -h, --help            show this help message and exit
  --gpu GPU, -g GPU
  --input INPUT, -i INPUT
  --output OUTPUT, -o OUTPUT
  --quality QUALITY, -q QUALITY
  --model_dir MODEL_DIR, -d MODEL_DIR
  --scale_ratio SCALE_RATIO, -s SCALE_RATIO
  --tta, -t
  --batch_size BATCH_SIZE, -b BATCH_SIZE
  --block_size BLOCK_SIZE, -l BLOCK_SIZE
  --extension {png,webp}, -e {png,webp}
  --arch {VGG7,0,UpConv7,1,ResNet10,2,UpResNet10,3}, -a {VGG7,0,UpConv7,1,ResNet10,2,UpResNet10,3}
  --method {noise,scale,noise_scale}, -m {noise,scale,noise_scale}
  --noise_level {0,1,2,3}, -n {0,1,2,3}
  --color {y,rgb}, -c {y,rgb}
  --tta_level {2,4,8}, -T {2,4,8}
  --width WIDTH, -W WIDTH
  --height HEIGHT, -H HEIGHT
  --shorter_side SHORTER_SIDE, -S SHORTER_SIDE
  --longer_side LONGER_SIDE, -L LONGER_SIDE
```

<!-- omit in toc -->
## Table of Contents

- [Help](#help)
- [Documentation](#documentation)
- [Install With PIP](#install-with-pip)
- [Language information](#language-information)
	- [Built for](#built-for)
- [Install Python on Windows](#install-python-on-windows)
	- [Chocolatey](#chocolatey)
	- [Windows - Python.org](#windows---pythonorg)
- [Install Python on Linux](#install-python-on-linux)
	- [Apt](#apt)
	- [Dnf](#dnf)
- [Install Python on MacOS](#install-python-on-macos)
	- [Homebrew](#homebrew)
	- [MacOS - Python.org](#macos---pythonorg)
- [How to run](#how-to-run)
	- [Windows](#windows)
	- [Linux/ MacOS](#linux-macos)
- [Building](#building)
- [Testing](#testing)
- [Download Project](#download-project)
	- [Clone](#clone)
		- [Using The Command Line](#using-the-command-line)
		- [Using GitHub Desktop](#using-github-desktop)
	- [Download Zip File](#download-zip-file)
- [Community Files](#community-files)
	- [Licence](#licence)
	- [Changelog](#changelog)
	- [Code of Conduct](#code-of-conduct)
	- [Contributing](#contributing)
	- [Security](#security)
	- [Support](#support)
	- [Rationale](#rationale)

## Documentation

A high-level overview of how the documentation is organized organized will help you know
where to look for certain things:

- [Tutorials](/documentation/tutorials) take you by the hand through a series of steps to get
  started using the software. Start here if you’re new.
- The [Technical Reference](/documentation/reference) documents APIs and other aspects of the
  machinery. This documentation describes how to use the classes and functions at a lower level
  and assume that you have a good high-level understanding of the software.
<!--
- The [Help](/documentation/help) guide provides a starting point and outlines common issues that you
  may have.
-->

## Install With PIP

```python
pip install waifu2x
```

Head to https://pypi.org/project/Waifu2x/ for more info

## Language information

### Built for

This program has been written for Python versions 3.8 - 3.11 and has been tested with both 3.8 and
3.11

## Install Python on Windows

### Chocolatey

```powershell
choco install python
```

### Windows - Python.org

To install Python, go to https://www.python.org/downloads/windows/ and download the latest
version.

## Install Python on Linux

### Apt

```bash
sudo apt install python3.x
```

### Dnf

```bash
sudo dnf install python3.x
```

## Install Python on MacOS

### Homebrew

```bash
brew install python@3.x
```

### MacOS - Python.org

To install Python, go to https://www.python.org/downloads/macos/ and download the latest
version.

## How to run

### Windows

- Module
	`py -3.x -m [module]` or `[module]` (if module installs a script)

- File
	`py -3.x [file]` or `./[file]`

### Linux/ MacOS

- Module
	`python3.x -m [module]` or `[module]` (if module installs a script)

- File
	`python3.x [file]` or `./[file]`

## Building

This project uses https://github.com/FHPythonUtils/FHMake to automate most of the building. This
command generates the documentation, updates the requirements.txt and builds the library artefacts

Note the functionality provided by fhmake can be approximated by the following

```sh
handsdown  --cleanup -o documentation/reference
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --with dev --output requirements_optional.txt
poetry build
```

`fhmake audit` can be run to perform additional checks

## Testing

For testing with the version of python used by poetry use

```sh
poetry run pytest
```

Alternatively use `tox` to run tests over python 3.8 - 3.11

```sh
tox
```

## Download Project

### Clone

#### Using The Command Line

1. Press the Clone or download button in the top right
2. Copy the URL (link)
3. Open the command line and change directory to where you wish to
clone to
4. Type 'git clone' followed by URL in step 2
	```bash
	git clone https://github.com/FHPythonUtils/Waifu2x
	```

More information can be found at
https://help.github.com/en/articles/cloning-a-repository

#### Using GitHub Desktop

1. Press the Clone or download button in the top right
2. Click open in desktop
3. Choose the path for where you want and click Clone

More information can be found at
https://help.github.com/en/desktop/contributing-to-projects/cloning-a-repository-from-github-to-github-desktop

### Download Zip File

1. Download this GitHub repository
2. Extract the zip archive
3. Copy/ move to the desired location

## Community Files

### Licence

MIT License
(See the [LICENSE](/LICENSE.md) for more information.)

### Changelog

See the [Changelog](/CHANGELOG.md) for more information.

### Code of Conduct

Online communities include people from many backgrounds. The *Project*
contributors are committed to providing a friendly, safe and welcoming
environment for all. Please see the
[Code of Conduct](https://github.com/FHPythonUtils/.github/blob/master/CODE_OF_CONDUCT.md)
 for more information.

### Contributing

Contributions are welcome, please see the
[Contributing Guidelines](https://github.com/FHPythonUtils/.github/blob/master/CONTRIBUTING.md)
for more information.

### Security

Thank you for improving the security of the project, please see the
[Security Policy](https://github.com/FHPythonUtils/.github/blob/master/SECURITY.md)
for more information.

### Support

Thank you for using this project, I hope it is of use to you. Please be aware that
those involved with the project often do so for fun along with other commitments
(such as work, family, etc). Please see the
[Support Policy](https://github.com/FHPythonUtils/.github/blob/master/SUPPORT.md)
for more information.

### Rationale

The rationale acts as a guide to various processes regarding projects such as
the versioning scheme and the programming styles used. Please see the
[Rationale](https://github.com/FHPythonUtils/.github/blob/master/RATIONALE.md)
for more information.
