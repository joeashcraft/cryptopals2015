#!env python3

import unittest

from set1_ch2 import c2

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.input_1 = '1c0111001f010100061a024b53535009181c'
        self.input_2 = '686974207468652062756c6c277320657965'
        self.expect_result = '0x746865206b696420646f6e277420706c6179'

    def test_decode(self):
        """ make sure the shuffled sequence does not lose any elements """
        self.assertEqual(
            c2(self.input_1, self.input_2),
            self.expect_result
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
