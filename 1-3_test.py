#!env python3

import unittest

from s1_c2 import c2
# from s1_c3 ...

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.input_1 = 'dead'
        self.input_2 = 'bbbb'
        self.expect_result = '0x6516''

    def test_decode(self):
        """ make sure the shuffled sequence does not lose any elements """
        self.assertEqual(
            c2(self.input_1, self.input_2),
            self.expect_result
        )

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
