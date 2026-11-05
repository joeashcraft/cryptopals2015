#!env python3
import unittest

from utils import equalize_lengths, xor


class TestEqualize_lengths(unittest.TestCase):
    def setUp(self):
        self.a = b"abcd"
        self.b_equal = b"wxyz"
        self.b_one = b"X"
        self.b_shorter = b"wxy"
        self.b_longer = b"wxyz1234"

    def test_equal_lengths_noop(self):
        self.assertEqual(
            equalize_lengths(self.a, self.b_equal),
            (self.a, self.b_equal),
        )

    def test_single_byte_b(self):
        self.assertEqual(
            equalize_lengths(self.a, self.b_one),
            (self.a, b"XXXX"),
        )

    def test_shorter_b(self):
        self.assertEqual(
            equalize_lengths(self.a, self.b_shorter),
            (self.a, b"wxyw"),
        )

    def test_longer_b(self):
        self.assertEqual(
            equalize_lengths(self.a, self.b_longer),
            (self.a, b"wxyz")
        )


class TestXor(unittest.TestCase):
    def setUp(self):
        self.input_1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
        self.input_2 = bytes.fromhex("686974207468652062756c6c277320657965")
        self.expect_result = bytes.fromhex(
            "746865206b696420646f6e277420706c6179"
        )

    def test_xor_equal_length(self):
        self.assertEqual(xor(self.input_1, self.input_2), self.expect_result)

    def test_xor_single_byte_key(self):
        self.assertEqual(xor(b"ICE", b"\x00"), b"ICE")
        self.assertEqual(xor(b"\x00\x00\x00", b"I"), b"III")

    def test_xor_repeating_key(self):
        # "ICE" repeated against plaintext, same as set1 challenge 5 idea
        plaintext = b"Burn"
        key = b"ICE"
        # B^I, u^C, r^E, n^I
        expected = bytes(
            [
                ord("B") ^ ord("I"),
                ord("u") ^ ord("C"),
                ord("r") ^ ord("E"),
                ord("n") ^ ord("I"),
            ]
        )
        self.assertEqual(xor(plaintext, key), expected)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
