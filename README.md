<h1 align="center">
  <br>
  <a href="https://github.com/HyperWinX/PyConstant">PyConstant</a>
</h1>

<h4 align="center">Simple library that provides lockable values</h4>

<p align="center">
    <a href="https://github.com/HyperWinX/PyConstant/issues">
    <img src="https://img.shields.io/github/issues/HyperWinX/PyConstant?color=lime"
         alt="GitHub opened issues">
    <img src="https://img.shields.io/badge/status-stable-lime"
         alt="Status">
    <img src="https://img.shields.io/github/license/HyperWinX/PyConstant?color=lime"
         alt="License">
    <img src="https://img.shields.io/github/stars/HyperWinX/PyConstant?color=lime"
         alt="Stars">
</p>

---
<table>
<tr>
<td>

**PyConstant** is a simple library, that provides implementation of lockable constant values.

</td>
</tr>
</table>

# Table of contents
- [Installation](#installation)
- [Usage](#usage)
    - [Creation](#creation)
    - [Lock constant](#lock-constant)
    - [Unlock constant](#unlock-constant)
    - [Check if constant is locked](#check-if-constant-is-locked)

## Installation
1. Download library itself: [constant.py](src/constant.py)
2. Import it
3. Use

## Usage

### Creation
Create constant:
```py
const = constant.Constant(5, False)
```
First argument - value of any type
Second argument defines if constant is locked.

### Lock constant
```py
const = constant.Constant(5, False)
const.lock()
```

### Unlock constant
```py
const = constant.Constant(5, False)
const.unlock()
```

### Check if constant is locked
```py
const = constant.Constant(5, False)
if (const.is_locked()):
  # Code
```

