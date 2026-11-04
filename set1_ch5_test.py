#!env python3

import unittest
import logging

from set1_ch5 import repeating_key_xor

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
#         self.plaintext = """Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal"""
        self.key = 'ICE'
        # self.ciphertext = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b 2f 20 43 0a 652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''
        self.ciphertext = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''



    def test_helpers(self):
        self.assertEqual(
            repeating_key_xor(self.plaintext, self.key),
            (self.ciphertext)
        )


    # def test_main(self):
    #     self.assertEqual(
    #         main(self.ciphertext),
    #         [(self.key, self.plaintext)]
    #     )

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
