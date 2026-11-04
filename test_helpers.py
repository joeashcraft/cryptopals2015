"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""

import unittest

from helpers import hex_to_b64, hex_xor


class Set1_Ch1(unittest.TestCase):
    def setUp(self):
        self.hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        self.expect_result = (
            "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        )

    def test_hex_to_b64(self):
        self.assertEqual(hex_to_b64(self.hex_string), self.expect_result)


class Set1_Ch2(unittest.TestCase):
    def setUp(self):
        self.input_1 = "1c0111001f010100061a024b53535009181c"
        self.input_2 = "686974207468652062756c6c277320657965"
        self.expect_result = "746865206b696420646f6e277420706c6179"

    def test_hex_xor(self):
        """make sure the shuffled sequence does not lose any elements"""
        self.assertEqual(
            hex_xor(self.input_1, self.input_2), bytes.fromhex(self.expect_result)
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
