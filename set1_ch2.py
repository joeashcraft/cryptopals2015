#!env python3
# Write a function that takes two equal-length buffers and produces their XOR combination.

import sys
import logging
from helpers import hex_xor

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    try:
        one = sys.argv[1]
        two = sys.argv[2]
    except IndexError:
        one = "1c0111001f010100061a024b53535009181c"
        two = "686974207468652062756c6c277320657965"

    logging.debug(f"one={one}")
    logging.debug(f"two={two}")
    print(hex_xor(one, two).hex())
