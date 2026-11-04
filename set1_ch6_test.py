#!env python3

import unittest
import logging

from set1_ch6 import hamming_distance, main as ch6, guess_keysize, blocks_by_keysize, transpose_blocks

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.string_a = "this is a test"
        self.string_b = "wokka wokka!!!"
        self.test_hamming_distance = 37

        self.plaintext = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""
        self.key = 'ICE'
        self.ciphertext = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''



    def test_helpers(self):
        self.assertEqual(
            hamming_distance(self.string_a, self.string_b),
            (self.test_hamming_distance)
        )

    def test_guess_keysize(self):
        self.assertEqual(
            guess_keysize(self.ciphertext, key_size_max=5, best_guesses=3),
            ([
                [3, 2.0],
                [4, 2.0],
                [5, 2.0],
            ] )
        )

    def test_blocks_by_keysize(self):
        self.ciphertext = b'abcdefghijkl'
        self.assertEqual(
            blocks_by_keysize(self.ciphertext, keysize=3),
            [b'abc', b'def', b'ghi', b'jkl']
        )
        self.assertEqual(
            blocks_by_keysize(self.ciphertext, keysize=5),
            [b'abcde', b'fghij', b'kl']
        )

    def test_transpose_blocks(self):
        blocks = [b'abc', b'def', b'ghi', b'jkl']
        self.assertEqual(
            transpose_blocks(blocks),
            [b'adgj', b'behk', b'cfil']
        )
        self.assertEqual(
            transpose_blocks(blocks_by_keysize(b'abcdefghijkl', keysize=3)),
            [b'adgj', b'behk', b'cfil']
        )


    # def test_main(self):
    #     self.assertEqual(
    #         ch6(puzzle_input_filename='set1_ch6-input.txt', key_size_max=5),
    #         self.string_a
    #     )

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    unittest.main(argv=['first-arg-is-ignored'], exit=False)
