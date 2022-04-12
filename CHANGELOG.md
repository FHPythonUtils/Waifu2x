# Changelog

All major and minor version changes will be documented in this file. Details of
patch-level version changes can be found in [commit messages](../../commits/master).

## 2022.1 - 2022/04/12

- Improve tests
- Code improvements (docs + typing)
- Move docs
- Update pre-commit

## 2022 - 2022/01/23

- Added tests
  ```sh
  $ poetry run py -m pytest test/test.py
  ===================================== test session starts ======================================

  collected 4 items

  test\test.py ....                                                                         [100%]

  ====================================== 4 passed in 16.80s ======================================
  ```
- Bump pillow version (CVE-2022-22815, CVE-2022-22816, CVE-2022-22817)
- Fix crash when image has no transparency

## 2021.2 - 2021/11/10

- pre-commit
- type-hinting (partial)
- code quality improvements

## 2021.1 - 2021/09/14

- fix alpha detection https://github.com/FHPythonUtils/Waifu2x/issues/1

## 2021 - 2021/04/15

- First release
