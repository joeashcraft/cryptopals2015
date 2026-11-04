#!env python3

import unittest

from set1_ch2 import c2, hex_xor

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.input_1 = '1c0111001f010100061a024b53535009181c'
        self.input_2 = '686974207468652062756c6c277320657965'
        self.expect_result = '0x746865206b696420646f6e277420706c6179'

    def test_hex_xor(self):
        """ make sure the shuffled sequence does not lose any elements """
        self.assertEqual(
            hex_xor(self.input_1, self.input_2),
            bytes.fromhex(self.expect_result[2:])
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
