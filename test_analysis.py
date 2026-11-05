#!env python3
import unittest
from string import ascii_uppercase

from analysis import ETAOIN, letter_counter, frequency_order, freq_scoring


class TestLetterCounter(unittest.TestCase):
    def setUp(self):
        self.perfect_message = (
            "EEEEEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTTTT"
            "AAAAAAAAAAAAAAAAAAAAAAAAOOOOOOOOOOOOOOOOOOOOOOO"
            "IIIIIIIIIIIIIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSS"
            "HHHHHHHHHHHHHHHHHHHRRRRRRRRRRRRRRRRRRDDDDDDDDDDDDDDDDD"
            "LLLLLLLLLLLLLLLLCCCCCCCCCCCCCCCUUUUUUUUUUUUUUMMMMMMMMMMMMM"
            "WWWWWWWWWWWWFFFFFFFFFFFGGGGGGGGGGYYYYYYYYYPPPPPPPPBBBBBBBVVVVVV"
            "KKKKKJJJJXXXQQZ"
        )
        self.letter_count_ETAOIN = {
            "E": 26,
            "T": 25,
            "A": 24,
            "O": 23,
            "I": 22,
            "N": 21,
            "S": 20,
            "H": 19,
            "R": 18,
            "D": 17,
            "L": 16,
            "C": 15,
            "U": 14,
            "M": 13,
            "W": 12,
            "F": 11,
            "G": 10,
            "Y": 9,
            "P": 8,
            "B": 7,
            "V": 6,
            "K": 5,
            "J": 4,
            "X": 3,
            "Q": 2,
            "Z": 1,
        }

    def test_perfect_message(self):
        self.assertEqual(
            letter_counter(self.perfect_message),
            self.letter_count_ETAOIN,
        )

    def test_case_insensitive(self):
        self.assertEqual(
            letter_counter("AaBb"),
            letter_counter("AABB"),
        )

    def test_ignores_non_letters(self):
        counts = letter_counter("A! B? C.")
        self.assertEqual(counts["A"], 1)
        self.assertEqual(counts["B"], 1)
        self.assertEqual(counts["C"], 1)
        self.assertEqual(counts["D"], 0)

    def test_no_letters_returns_false(self):
        self.assertEqual(letter_counter("123!@#"), False)


class TestFrequencyOrder(unittest.TestCase):
    def setUp(self):
        # fmt: off
        self.letter_count_ETAOIN = {
            "E": 26, "T": 25, "A": 24, "O": 23, "I": 22, "N": 21,
            "S": 20, "H": 19, "R": 18, "D": 17, "L": 16, "C": 15,
            "U": 14, "M": 13, "W": 12, "F": 11, "G": 10, "Y": 9,
            "P": 8, "B": 7, "V": 6, "K": 5, "J": 4, "X": 3,
            "Q": 2, "Z": 1,
        }
        # fmt: off
        self.letter_count_random_in = {
            "O": 26, "D": 25, "E": 24, "B": 23, "U": 22, "I": 21,
            "R": 20, "J": 19, "A": 18, "G": 17, "X": 16, "F": 15,
            "Y": 14, "T": 13, "K": 12, "M": 11, "Q": 10, "L": 9,
            "H": 8, "V": 7, "P": 6, "Z": 5, "N": 4, "W": 3,
            "S": 2, "C": 1,
        }
        self.letter_count_random_expected = "ODEBUIRJAGXFYTKMQLHVPZNWSC"

    def test_etaoin_order(self):
        self.assertEqual(frequency_order(self.letter_count_ETAOIN), ETAOIN)

    def test_random_order(self):
        self.assertEqual(
            frequency_order(self.letter_count_random_in),
            self.letter_count_random_expected,
        )


class TestFreqScoring(unittest.TestCase):
    def setUp(self):
        self.letter_count_random_expected = "ODEBUIRJAGXFYTKMQLHVPZNWSC"

    def test_perfect_etaoin(self):
        self.assertEqual(freq_scoring(ETAOIN), 100)

    def test_random_order(self):
        self.assertEqual(freq_scoring(self.letter_count_random_expected), 3 + 1)

    def test_garbage(self):
        self.assertEqual(freq_scoring("\x101)~*6?*~*6;~.?,*'~7-~4+3.709T"), 0)

    def test_ascii_uppercase(self):
        # ABCDEF ∩ ETAOIN = A,E (2); UVWXYZ ∩ VKJXQZ = V,X,Z (3)
        self.assertEqual(freq_scoring(ascii_uppercase), 5)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
