#!env python3

import unittest

from set1_ch3 import c3, main, equalize_lengths

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.plaintext = 'dead'
        self.key = 'b'
        self.ciphertext = '0x6516'

    def test_helpers(self):
        self.assertEqual(
            equalize_lengths('aaa', 'b'),
            ('aaa', 'bbb')
        )
        
    def test_main(self):
        self.assertEqual(
            main(self.ciphertext),
            [(self.key, self.plaintext)]
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
