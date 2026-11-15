#!env python3
import unittest

import utils


class TestEqualize_lengths(unittest.TestCase):
    def setUp(self):
        self.a = b"abcd"
        self.b_equal = b"wxyz"
        self.b_one = b"X"
        self.b_shorter = b"wxy"
        self.b_longer = b"wxyz1234"

    def test_equal_lengths_noop(self):
        self.assertEqual(
            utils.equalize_lengths(self.a, self.b_equal),
            (self.a, self.b_equal),
        )

    def test_single_byte_b(self):
        self.assertEqual(
            utils.equalize_lengths(self.a, self.b_one),
            (self.a, b"XXXX"),
        )

    def test_shorter_b(self):
        self.assertEqual(
            utils.equalize_lengths(self.a, self.b_shorter),
            (self.a, b"wxyw"),
        )

    def test_longer_b(self):
        self.assertEqual(
            utils.equalize_lengths(self.a, self.b_longer), (self.a, b"wxyz")
        )


class TestXor(unittest.TestCase):
    def setUp(self):
        self.input_1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
        self.input_2 = bytes.fromhex("686974207468652062756c6c277320657965")
        self.expect_result = bytes.fromhex(
            "746865206b696420646f6e277420706c6179"
        )

    def test_xor_equal_length(self):
        self.assertEqual(utils.xor(self.input_1, self.input_2), self.expect_result)

    def test_xor_single_byte_key(self):
        self.assertEqual(utils.xor(b"ICE", b"\x00"), b"ICE")
        self.assertEqual(utils.xor(b"\x00\x00\x00", b"I"), b"III")

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
        self.assertEqual(utils.xor(plaintext, key), expected)


class TestSingleByteXorSolve(unittest.TestCase):
    def setUp(self):
        self.ciphertext = bytes.fromhex("190c0c191b1358190c581c190f16")
        self.expected = ("x", b"attack at dawn", "ATCDKNWBEFGHIJLMOPQRSUVXYZ", 6)

    def test_single_byte_xor_solve(self):
        self.assertEqual(utils.single_byte_xor_solve(self.ciphertext)[0], self.expected)


if __name__ == "__main__":  # pragma: no cover
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
