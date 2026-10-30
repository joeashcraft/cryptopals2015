#!env python3

import unittest

from set1_ch3 import c3, main, equalize_lengths, frequency_order, letter_counter, freq_scoring, ETAOIN

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.plaintext = 'dead'
        self.key = 'b'
        self.ciphertext = '6516'  # not '0x6516'
        
        self.perfect_message=(
            'EEEEEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTTTT'
            'AAAAAAAAAAAAAAAAAAAAAAAAOOOOOOOOOOOOOOOOOOOOOOO'
            'IIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSS'
            'HHHHHHHHHHHHHHHHHHHRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDD'
            'LLLLLLLLLLLLLLLLCCCCCCCCCCCCCCCUUUUUUUUUUUUUUMMMMMMMMMMMMM'
            'WWWWWWWWWWWWFFFFFFFFFFFGGGGGGGGGGYYYYYYYYYPPPPPPPPBBBBBBBVVVVVV'
            'KKKKKJJJJXXXQQZ'
        )
        self.letter_count_ETAOIN = {
            'E': 26, 'T': 25, 'A': 24, 'O': 23, 'I': 22, 'N': 21, 'S': 20,
            'H': 19, 'R': 18, 'D': 17, 'L': 16, 'C': 15, 'U': 14, 'M': 13,
            'W': 12, 'F': 11, 'G': 10, 'Y': 9, 'P': 8, 'B': 7, 'V': 6, 'K': 5,
            'J': 4, 'X': 3, 'Q': 2, 'Z': 1
        }
        self.letter_count_reverse_ETAOIN = {
            'E': 0, 'T': 1, 'A': 2, 'O': 3, 'I': 4, 'N': 5, 'S': 6, 'H': 7,
            'R': 8, 'D': 9, 'L': 10, 'C': 11, 'U': 12, 'M': 13, 'W': 14,
            'F': 15, 'G': 16, 'Y': 17, 'P': 18, 'B': 19, 'V': 20, 'K': 21,
            'J': 22, 'X': 23, 'Q': 24, 'Z': 25
        }

        self.letter_count_random_in = {
            'O': 26, 'D': 25, 'E': 24, 'B': 23, 'U': 22, 'I': 21, 'R': 20,
            'J': 19, 'A':18, 'G': 17, 'X': 16, 'F': 15, 'Y': 14, 'T': 13,
            'K': 12, 'M': 11, 'Q': 10, 'L': 9, 'H': 8, 'V': 7, 'P': 6, 'Z': 5,
            'N': 4, 'W': 3, 'S': 2, 'C': 1
        }
        self.letter_count_random_expected = 'ODEBUIRJAGXFYTKMQLHVPZNWSC'



    def test_helpers(self):
        self.assertEqual(
            equalize_lengths('aaa', 'b'),
            ('aaa', 'bbb')
        )
        self.assertEqual(
            frequency_order(self.letter_count_ETAOIN),
            ETAOIN
        )
        self.assertEqual(
            frequency_order(self.letter_count_random_in), 
            self.letter_count_random_expected,
            'frequency_order with random shuffled input'
        )
        self.assertEqual(
            letter_counter(self.perfect_message),
            self.letter_count_ETAOIN,
            'letter_counter with a perfectly representative message'
        )
        self.assertEqual(freq_scoring(ETAOIN), 100, 'score of ETAOIN itself')
        self.assertEqual(freq_scoring(self.letter_count_random_expected), 3+1)
        self.assertEqual(freq_scoring("\x101)~*6?*~*6;~.?,*'~7-~4+3.709T"), 0)
        
    # def test_main(self):
    #     self.assertEqual(
    #         main(self.ciphertext),
    #         [(self.key, self.plaintext)]
    #     )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
