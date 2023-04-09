import unittest
from colortools.color_converter import rgb_to_hex

class ColorConverterTestCase(unittest.TestCase):
    def test_rgb_to_hex(self):
        # Test case 1: Valid RGB values
        rgb = (255, 255, 255)
        expected = "#ffffff"
        result = rgb_to_hex(rgb)
        self.assertEqual(result, expected)

        # Test case 2: Invalid RGB values
        rgb = (256, 0, -1)
        with self.assertRaises(ValueError):
            rgb_to_hex(rgb)