from colortools.color_converter import rgb_to_lab
import math


def ciede2000(lab1, lab2):
    """
    Calculate the CIEDE2000 color difference between two LAB tuples.
    
    Args:
        lab1 (tuple): LAB tuple for the first color, in the format (L, a, b).
        lab2 (tuple): LAB tuple for the second color, in the format (L, a, b).
        
    Returns:
        float: The CIEDE2000 color difference between the two colors.
    """
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    
    # Constants
    kL = 1
    kC = 1
    kH = 1
    
    # Calculate CIEDE2000 components
    deltaL = L2 - L1
    Lmean = (L1 + L2) / 2
    C1 = math.sqrt(a1**2 + b1**2)
    C2 = math.sqrt(a2**2 + b2**2)
    Cmean = (C1 + C2) / 2
    deltaC = C2 - C1
    deltaH = math.sqrt(max(0, (a2-a1)**2 + (b2-b1)**2 - deltaC**2))
    H1_rad = math.atan2(b1, a1)
    H1_deg = math.degrees(H1_rad) % 360
    H2_rad = math.atan2(b2, a2)
    H2_deg = math.degrees(H2_rad) % 360
    
    # Calculate hue difference
    if abs(H1_deg - H2_deg) <= 180:
        deltaH = H2_deg - H1_deg
    else:
        if H2_deg <= H1_deg:
            deltaH = H2_deg - H1_deg + 360
        else:
            deltaH = H2_deg - H1_deg - 360
            
    deltaH = 2 * math.sqrt(C1 * C2) * math.sin(math.radians(deltaH) / 2)
    
    # Calculate weighting factors
    SL = 1
    SC = 1 + 0.045 * Cmean
    SH = 1 + 0.015 * Cmean * (1 - 0.17 * math.cos(math.radians(deltaH - 30))) / (1 - 0.56 * math.cos(math.radians(deltaH - 30)))
    
    # Calculate CIEDE2000
    deltaL /= (kL * SL)
    deltaC /= (kC * SC)
    deltaH /= (kH * SH)
    
    deltaE2000 = math.sqrt(deltaL**2 + deltaC**2 + deltaH**2)
    
    return deltaE2000

def cie76(lab1, lab2):
    """
    Calculate the color difference (Delta E*76) between two CIELAB color tuples using the CIE76 formula.
    
    Args:
        lab1 (tuple): The first CIELAB color tuple in the form (L, a, b).
        lab2 (tuple): The second CIELAB color tuple in the form (L, a, b).
        
    Returns:
        float: The color difference (Delta E*76) between the two colors.
    """
    delta_L = lab1[0] - lab2[0]
    delta_a = lab1[1] - lab2[1]
    delta_b = lab1[2] - lab2[2]
    
    delta_E = math.sqrt(delta_L**2 + delta_a**2 + delta_b**2)
    
    return delta_E

def cie94(lab1, lab2):
    """
    Calculates the CIE94 color difference between two CIELAB tuples.

    Args:
        lab1 (tuple): A tuple containing the L, a, and b values of the first color in CIELAB format.
        lab2 (tuple): A tuple containing the L, a, and b values of the second color in CIELAB format.

    Returns:
        float: The CIE94 color difference between the two colors.
    """
    l1, a1, b1 = lab1
    l2, a2, b2 = lab2

    delta_l = l1 - l2
    delta_a = a1 - a2
    delta_b = b1 - b2

    c1 = math.sqrt(a1 ** 2 + b1 ** 2)
    c2 = math.sqrt(a2 ** 2 + b2 ** 2)
    delta_c = c1 - c2

    delta_h_sq = delta_a ** 2 + delta_b ** 2 - delta_c ** 2
    delta_h = math.sqrt(max(0, delta_h_sq))

    k_l = 1
    k_c = 1
    k_h = 1

    k1 = 0.045
    k2 = 0.015

    sl = 1
    kc = 1
    kh = 1

    if c1 * c2 != 0:
        sl = 1 + k1 * delta_l / (k_l * c1)
        kc = 1 + k2 * delta_c / (k_c * c1)
        kh = 1 + k2 * delta_h / (k_h * c1)

    return math.sqrt((delta_l / (k_l * sl)) ** 2 + (delta_c / (k_c * kc)) ** 2 + (delta_h / (k_h * kh)) ** 2)


def ciede2000_rgb(rgb1, rgb2):
    lab1 = rgb_to_lab(rgb1)
    lab2 = rgb_to_lab(rgb2)
    return ciede2000(lab1, lab2)

def cie76_rgb(rgb1, rgb2):
    lab1 = rgb_to_lab(rgb1)
    lab2 = rgb_to_lab(rgb2)
    return cie76(lab1, lab2)

def cie94_rgb(rgb1, rgb2):
    lab1 = rgb_to_lab(rgb1)
    lab2 = rgb_to_lab(rgb2)
    return cie94(lab1, lab2)

print(cie94_rgb((200,200,200), (0,0,0)))
