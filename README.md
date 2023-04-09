# Colortools
Python package for common color conversions and operations

## Description
Python package for conversions between common color representations like RGB and HEX and color comparisons using CIE formulas.

## Features
### Conversion between common color represantations
- RGB
- HEX
- CMYK
- HSL
- HSV
- LAB
- XYZ
### Color difference calculation (Delta E)
> measure of the perceptual difference between two colors
- Delta E (ΔE) CIE76 Formula
- Delta E (ΔE) CIE94 Formula
- Delta E (ΔE) CIEDE2000 Formula

## Quickstart
### Installation 
To install from PyPI with pip:

```bash
$ python -m pip install colortools
```

### Example usage: 
Using colortools in a Python script to calculate the CIEDE200 difference between to hex colors.
```python
from colortools import color_converter, color_utils
color1 = color_converter.hex_to_rgb("#ddf4ee")
coor2 = color_converter.hex_to_rgb("#88bfb1")
deltaE = color_utils.CIEDE2000_rgb(color1, color2)
```

## Documentation
all color models are represented as tuples except hex codes: e.g: (255,255,255)
### color_converter:
syntax: colortools.color_converter.hex_to_rgb(hex)

supported color models: rgb, hex, cmyk, hsl, hsv, lab, xyz

### color_utils: 
includes CIE functions to calculate the Delta E difference between to colors (perceptual difference).

- ciede2000(lab1, lab2)
- ciede2000_rgb(rgb1, rgb2)
- cie76(lab1, lab2)
- cie76_rgb(rgb1, rgb2)
- cie94(lab1, lab2)
- cie94_rgb(rgb1, rgb2)

returns Delta E as float

