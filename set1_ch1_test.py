"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import random
import unittest

from set1_ch1 import hex_to_b64

class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        self.expect_result = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    def test_decode(self):
        """ make sure the shuffled sequence does not lose any elements """
        self.assertEqual(
            hex_to_b64(self.hex_string),
            self.expect_result
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
