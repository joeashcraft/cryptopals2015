#!/usr/bin/env python3
"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""

import unittest

from helpers import (
    ascii_to_binary,
    ascii_to_hex,
    bytes_to_binary,
    hex_string_to_ascii_string,
    hex_to_b64,
    hex_xor,
)

ABC_ASCII = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ABC_HEX = "4142434445464748494a4b4c4d4e4f505152535455565758595a"
ABC_BINARY = "01000001 01000010 01000011 01000100 01000101 01000110 01000111 01001000 01001001 01001010 01001011 01001100 01001101 01001110 01001111 01010000 01010001 01010010 01010011 01010100 01010101 01010110 01010111 01011000 01011001 01011010"
ABC_B64 = "QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo="

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


class TestHelpers(unittest.TestCase):

    def test_ascii_to_hex(self):
        self.assertEqual(ascii_to_hex(ABC_ASCII), ABC_HEX)

    def test_ascii_to_binary(self):
        self.assertEqual(ascii_to_binary(ABC_ASCII), ABC_BINARY)

    def test_bytes_to_binary(self):
        self.assertEqual(bytes_to_binary(ABC_ASCII.encode()), ABC_BINARY)

    def test_hex_string_to_ascii_string(self):
        self.assertEqual(hex_string_to_ascii_string(ABC_HEX), ABC_ASCII)
        self.assertEqual(hex_string_to_ascii_string("0x" + ABC_HEX), ABC_ASCII)

    def test_hex_to_b64(self):
        self.assertEqual(hex_to_b64(ABC_HEX), ABC_B64)


if __name__ == "__main__":  # pragma: no cover
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
