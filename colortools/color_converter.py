# hex operations

def _expand_hex(hex_code):
    """
    Doubles every character of the hex code
    """
    return "".join([char * 2 for char in hex_code])

def _validate_hex(hex_code):
    """
    Check if the hex code is a valid hexadecimal RGB(A) code
    """
    if not all(c in "0123456789ABCDEFabcdef" for c in hex_code) or (len(hex_code) != 6 and len(hex_code) != 8):
        raise ValueError("Input is not a valid hexadecimal RGB(A) code")

def _format_hex(hex_code):
    """
    format the hex code
    """
    # Remove the "#" symbol if present
    if hex_code.startswith("#"):
        hex_code = hex_code[1:]

    # expand hex if needed
    if len(hex_code) == 3 or len(hex_code) == 4:
        hex_code = _expand_hex(hex_code)

    # validate hex
    _validate_hex(hex_code)
    
    return hex_code


# rgb operations

def _validate_rgb(rgb):
    """
    validate the rgb(a) values
    """ 
    # Check if the input is a tuple of length 3 or 4
    if not isinstance(rgb, tuple) or (len(rgb) != 3 and len(rgb) != 4):
        raise ValueError("Input should be a tuple of three or four integers representing RGB(A) values.")
    
    # Check if each RGB value is within the valid range [0, 255]
    for value in rgb:
        if not isinstance(value, int) or value < 0 or value > 255:
            raise ValueError("RGB values should be integers in the range [0, 255].")

# conversions

def rgb_to_hex(rgb: tuple) -> str:
    """
    Convert RGB(A) color values to hexadecimal color code.

    Args:
        rgb(A) (tuple): Tuple of three or four integers representing RGB(A) values. Each value should be in the range [0, 255].

    Returns:
        str: Hexadecimal color code.

    """
    # validate
    _validate_rgb(rgb)

    # Convert RGB to hexadecimal
    hex_color = "#" + "".join(f"{i:02x}" for i in rgb)

    return hex_color

def hex_to_rgb(hex_code: str) -> tuple:
    """
    Convert a valid hexadecimal RGB(A) code to RGB values.
    
    Args:
    - hex_code (str): A string containing a valid hexadecimal RGB(A) code.
    
    Returns:
    - tuple: A tuple containing the RGB values as integers in the format (R, G, B).
    
    Raises:
    - ValueError: If the input hex code is not a valid hexadecimal RGB(A) code.
    """
    # format the hex code
    hex_code =_format_hex(hex_code)
    
    # Convert the hex code to RGB values
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    
    return (r, g, b)

def hex_to_rgba(hex_code: str) -> tuple:
    """
    Convert a valid hexadecimal RGB(A) code to RGBA values.
    
    Args:
    - hex_code (str): A string containing a valid hexadecimal RGB(A) code.
    
    Returns:
    - tuple: A tuple containing the RGBA values as integers in the format (R, G, B, A).
    
    Raises:
    - ValueError: If the input hex code is not a valid hexadecimal RGB(A) code.
    """
    # format the hex code
    hex_code =_format_hex(hex_code)
    
    # Convert the hex code to RGB values
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    a = int(hex_code[6:8], 16) if len(hex_code) == 8 else 255
    
    return (r, g, b, a)

def rgb_to_rgba(rgb: tuple) -> tuple:
    """
    Convert RGB values to RGBA values.

    Args:
    - RGB(A) (tuple): Tuple of three or four integers representing RGB(A) values. Each value should be in the range [0, 255].

    Returns:
    - tuple: A tuple containing the RGBA values as integers in the format (R, G, B, A).
    """
    # validate input
    _validate_rgb(rgb)

    # If input has three values, add default alpha value (255) and return as RGBA tuple
    if len(rgb) == 3:
        return (rgb[0], rgb[1], rgb[2], 255)
    
    # If input already has four values, return as RGBA tuple
    return rgb

def rgba_to_rgb(rgba: tuple) -> tuple:
    """
    Convert RGBA values to RGB values.

    Args:
    - RGB(A) (tuple): Tuple of three or four integers representing RGB(A) values. Each value should be in the range [0, 255].

    Returns:
    - tuple: A tuple containing the RGBA values as integers in the format (R, G, B, A).
    """
    # validate input
    _validate_rgb(rgba)

    return (rgba[0], rgba[1], rgba[2])

def _val_rgb(rgb):
    if len(rgb) > 3:
        return (rgb[0], rgb[1], rgb[2])

def hex_to_hsl(hex: str) -> tuple:
    """
    Convert HEX values to HSL values.

    Args:
    - HEX Code (str).

    Returns:
    - tuple: A tuple containing the HSL values.
    """
    rgb = hex_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_hsl(rgb)

def hex_to_cmyk(hex: str) -> tuple:
    """
    Convert HEX values to CMYK values.

    Args:
    - HEX (str)

    Returns:
    - tuple: A tuple containing the CMYK values
    """
    rgb = hex_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_cmyk(rgb)

def hex_to_hsl(hex: str) -> tuple:
    """
    Convert HEX values to HSV values.

    Args:
    - HEX (str)

    Returns:
    - tuple: A tuple containing the HSV values
    """
    rgb = hex_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_hsv(rgb)

def hex_to_lab(hex: str) -> tuple:
    """
    Convert HEX values to LAB values.

    Args:
    - HEX (str)

    Returns:
    - tuple: A tuple containing the LAB values
    """
    rgb = hex_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_lab(rgb)

def hex_to_lab(hex: str) -> tuple:
    """
    Convert HEX values to XYZ values.

    Args:
    - HEX (str)

    Returns:
    - tuple: A tuple containing the XYZ values
    """
    rgb = hex_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_xyz(rgb)

def rgb_to_hsl(rgb: tuple) -> tuple:
    """
    Convert RGB values to HSL values.

    Args:
    - RGB (tuple): Tuple of three integers representing RGB values. Each value should be in the range [0, 255].

    Returns:
    - tuple: A tuple containing the HSL values as integers in the format (H, S, L).
    """
    # validate input
    _validate_rgb(rgb)
    if len(rgb) == 4:
        rgb = (rgb[0], rgb[1], rgb[2])

    # Normalize RGB values to the range [0, 1]
    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0

    max_val = max(r, g, b)
    min_val = min(r, g, b)
    diff = max_val - min_val

    # Calculate Hue
    if diff == 0:
        h = 0
    elif max_val == r:
        h = (60 * ((g - b) / diff) + 360) % 360
    elif max_val == g:
        h = (60 * ((b - r) / diff) + 120) % 360
    elif max_val == b:
        h = (60 * ((r - g) / diff) + 240) % 360

    # Calculate Lightness
    l = ((max_val + min_val) / 2) * 100

    # Calculate Saturation
    if diff == 0:
        s = 0
    else:
        s = (diff / (1 - abs(2 * l / 100 - 1))) * 100

    return round(h), round(s), round(l)

def hsl_to_rgb(hsl: tuple) -> tuple:
    """
    Convert HSL values to RGB values.

    Args:
    - HSL (tuple): Tuple of three integers representing HSL values.  
        h (float): Hue value in the range [0, 360]
        s (float): Saturation value in the range [0, 1]
        l (float): Lightness value in the range [0, 1]


    Returns:
    - tuple: A tuple containing the RGB values as integers in the format (R, G, B).

    Raises:
        ValueError: If any of the input values are outside the valid range.
    """
    h, s, l = hsl
    s /= 100.0
    l/= 100.0

    # Validate input values
    if not 0 <= h <= 360:
        raise ValueError("Hue value must be in the range [0, 360]")
    if not 0 <= s <= 1:
        raise ValueError("Saturation value must be in the range [0, 1]")
    if not 0 <= l <= 1:
        raise ValueError("Lightness value must be in the range [0, 1]")

    # Convert hue to the range [0, 1]
    h = h / 360.0

    # Calculate chroma
    c = (1 - abs(2 * l - 1)) * s

    # Calculate intermediate values
    x = c * (1 - abs((h * 6) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 1 / 6:
        r, g, b = c, x, 0
    elif 1 / 6 <= h < 2 / 6:
        r, g, b = x, c, 0
    elif 2 / 6 <= h < 3 / 6:
        r, g, b = 0, c, x
    elif 3 / 6 <= h < 4 / 6:
        r, g, b = 0, x, c
    elif 4 / 6 <= h < 5 / 6:
        r, g, b = x, 0, c
    else:
        r, g, b = c, 0, x

    # Convert RGB values to the range [0, 255]
    r = int((r + m) * 255)
    g = int((g + m) * 255)
    b = int((b + m) * 255)

    return r, g, b

def hsl_to_cmyk(hsl: tuple) -> tuple:
    """
    Convert HSL values to CMYK values.

    Args:
    - HSL (tuple)

    Returns:
    - tuple: A tuple containing the CMYK values
    """
    rgb = hsl_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_cmyk(rgb)

def hsl_to_hsv(hsl: tuple) -> tuple:
    """
    Convert HSL values to HSV values.

    Args:
    - HSL (tuple)

    Returns:
    - tuple: A tuple containing the HSV values
    """
    rgb = hsl_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_hsl(rgb)

def hsl_to_lab(hsl: tuple) -> tuple:
    """
    Convert HSL values to LAB values.

    Args:
    - HSL (tuple)

    Returns:
    - tuple: A tuple containing the LAB values
    """
    rgb = hsl_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_lab(rgb)

def hsl_to_xyz(hsl: tuple) -> tuple:
    """
    Convert HSL values to XYZ values.

    Args:
    - HSL (tuple)

    Returns:
    - tuple: A tuple containing the XYZ values
    """
    rgb = hsl_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_xyz(rgb)

def rgb_to_cmyk(rgb: tuple) -> tuple:
    """
    Converts an RGB tuple to CMYK tuple.
    
    Args:
        rgb (tuple): RGB tuple (red, green, blue) with values between 0 and 255.
        
    Returns:
        tuple: CMYK tuple (cyan, magenta, yellow, black) with values between 0 and 100.
    """
    # validate rgb
    _validate_rgb(rgb)
    if len(rgb) == 4:
        rgb = (rgb[0], rgb[1], rgb[2])

    r, g, b = rgb
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    k = 1 - max(r, g, b)
    c = (1 - r - k) / (1 - k) if (1 - k) != 0 else 0
    m = (1 - g - k) / (1 - k) if (1 - k) != 0 else 0
    y = (1 - b - k) / (1 - k) if (1 - k) != 0 else 0
    
    return round(c * 100), round(m * 100), round(y * 100), round(k * 100)

def cmyk_to_rgb(cmyk: tuple) -> tuple:
    """
    Convert CMYK tuple to RGB tuple.
    
    Args:
        cmyk (tuple): CMYK values as a tuple of floats (Cyan, Magenta, Yellow, Black) in the range [0, 100].
        
    Returns:
        tuple: RGB values as a tuple of integers (Red, Green, Blue) in the range [0, 255].
    """
    c, m, y, k = cmyk
    c = c / 100.0
    m = m / 100.0
    y = y / 100.0
    k = k / 100.0

    # validation
    if len(cmyk) != 4:
        raise ValueError("CMYK tuple must contain exactly for integers")
    if not all(0 <= val <= 100 for val in cmyk):
        raise ValueError("CMYK values must be within the range of 0 to 100")

    # Convert CMYK to RGB using the formula
    r = round((1 - c) * (1 - k) * 255)
    g = round((1 - m) * (1 - k) * 255)
    b = round((1 - y) * (1 - k) * 255)
    
    return r, g, b

def cmyk_to_hsv(cmyk: tuple) -> tuple:
    """
    Convert CMYK values to HSV values.

    Args:
    - CMYK (tuple)

    Returns:
    - tuple: A tuple containing the HSV values
    """
    rgb = cmyk_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_hsv(rgb)

def cmyk_to_lab(cmyk: tuple) -> tuple:
    """
    Convert CMYK values to LAB values.

    Args:
    - CMYK (tuple)

    Returns:
    - tuple: A tuple containing the LAB values
    """
    rgb = cmyk_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_lab(rgb)

def cmyk_to_xyz(cmyk: tuple) -> tuple:
    """
    Convert CMYK values to XYZ values.

    Args:
    - CMYK (tuple)

    Returns:
    - tuple: A tuple containing the XYZ values
    """
    rgb = cmyk_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_xyz(rgb)

def hsv_to_lab(hsv: tuple) -> tuple:
    """
    Convert HSV values to LAB values.

    Args:
    - HSV (tuple)

    Returns:
    - tuple: A tuple containing the LAB values
    """
    rgb = hsv_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_lab(rgb)

def hsv_to_xyz(hsv: tuple) -> tuple:
    """
    Convert HSV values to XYZ values.

    Args:
    - HSV (tuple)

    Returns:
    - tuple: A tuple containing the XYZ values
    """
    rgb = hsv_to_rgb(hex)    
    rgb = _val_rgb(rgb)
    return rgb_to_xyz(rgb)


def rgb_to_hsv(rgb: tuple) -> tuple:
    """
    Convert RGB values to HSV values.

    Args:
    - RGB (tuple): Tuple of three integers representing RGB values. Each value should be in the range [0, 255].

    Returns:
    - tuple: A tuple containing the HSV values as integers in the format (H, S, V).
    """
    # validate input
    _validate_rgb(rgb)
    if len(rgb) == 4:
        rgb = (rgb[0], rgb[1], rgb[2])

    r, g, b = rgb
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    max_value = max(r, g, b)
    min_value = min(r, g, b)
    delta = max_value - min_value

    if delta == 0:
        hue = 0
    elif max_value == r:
        hue = ((g - b) / delta) % 6
    elif max_value == g:
        hue = ((b - r) / delta) + 2
    else:
        hue = ((r - g) / delta) + 4

    hue *= 60

    if hue < 0:
        hue += 360

    if max_value == 0:
        saturation = 0
    else:
        saturation = (delta / max_value) * 100

    value = max_value * 100

    hsv = (round(hue), round(saturation), round(value))
    return hsv

def hsv_to_rgb(hsv: tuple) -> tuple:
    """
    Convert HSV values to RGB values.

    Args:
    - HSV (tuple): Tuple of three integers representing HSV values.

    Returns:
    - tuple: A tuple containing the RGB values as integers in the format (R, G, B).
    """
    hue, saturation, value = hsv
    print(saturation)
    # Validate input values
    if not 0 <= hue <= 360:
        raise ValueError("Hue value must be in the range [0, 360]")
    if not 0 <= saturation <= 100:
        raise ValueError("Saturation value must be in the range [0, 100]")
    if not 0 <= value <= 100:
        raise ValueError("Lightness value must be in the range [0, 100]")
    
    hue /= 360.0
    saturation /= 100.0
    value /= 100.0
    
    if saturation == 0.0:
        # If saturation is 0, the color is grayscale (achromatic)
        return int(value * 255), int(value * 255), int(value * 255)
    
    h_i = int(hue * 6)
    f = hue * 6 - h_i
    p = value * (1 - saturation)
    q = value * (1 - f * saturation)
    t = value * (1 - (1 - f) * saturation)
    
    if h_i == 0:
        r, g, b = value, t, p
    elif h_i == 1:
        r, g, b = q, value, p
    elif h_i == 2:
        r, g, b = p, value, t
    elif h_i == 3:
        r, g, b = p, q, value
    elif h_i == 4:
        r, g, b = t, p, value
    else:
        r, g, b = value, p, q
        
    return int(r * 255), int(g * 255), int(b * 255)

   

# CIE

def rgb_to_xyz(rgb: tuple) -> tuple:
    """
    Convert RGB color values to XYZ color space.

    Args:
        rgb (tuple): RGB color values as a tuple (R, G, B) where each value is in the range [0, 255].

    Returns:
        tuple: XYZ color values as a tuple (X, Y, Z) where each value is a decimal number.
    """
    # Normalize RGB values to the range [0, 1]
    r = rgb[0] / 255.0
    g = rgb[1] / 255.0
    b = rgb[2] / 255.0

    # Apply gamma correction to linearize RGB values
    r = _apply_gamma_correction(r)
    g = _apply_gamma_correction(g)
    b = _apply_gamma_correction(b)

    # Apply transformation matrix to convert RGB to XYZ
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    # Convert XYZ values from linear to decimal format
    x *= 100.0
    y *= 100.0
    z *= 100.0

    return x, y, z

def _apply_gamma_correction(value):
    """
    Apply gamma correction to a color value.

    Args:
        value (float): Color value to be gamma corrected.

    Returns:
        float: Gamma corrected color value.
    """
    if value <= 0.04045:
        value /= 12.92
    else:
        value = ((value + 0.055) / 1.055) ** 2.4
    return value

def rgb_to_lab(rgb: tuple) -> tuple:
    xyz = rgb_to_xyz(rgb)
    lab = xyz_to_lab(xyz)
    return lab

def xyz_to_lab(xyz: tuple) -> tuple:
    """
    Convert XYZ color values to LAB color space.

    Args:
        xyz (tuple): XYZ color values as a tuple (X, Y, Z) where each value is a decimal number.

    Returns:
        tuple: LAB color values as a tuple (L, a, b) where each value is a decimal number.
    """
    # Reference white point for D65 illuminant
    Xn, Yn, Zn = 95.047, 100.000, 108.883

    # Normalize XYZ values
    xn = xyz[0] / Xn
    yn = xyz[1] / Yn
    zn = xyz[2] / Zn

    # Apply non-linear transformation to XYZ values
    xn = _apply_lab_transformation(xn)
    yn = _apply_lab_transformation(yn)
    zn = _apply_lab_transformation(zn)

    # Calculate LAB values
    l = max(0.0, 116.0 * yn - 16.0)
    a = (xn - yn) * 500.0
    b = (yn - zn) * 200.0

    return l, a, b

def _apply_lab_transformation(value):
    """
    Apply non-linear transformation to a color value for LAB conversion.

    Args:
        value (float): Color value to be transformed.

    Returns:
        float: Transformed color value.
    """
    if value > 0.008856:
        value = value ** (1.0 / 3.0)
    else:
        value = (value * 903.3 + 16.0) / 116.0
    return value

