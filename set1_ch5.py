#!/usr/bin/env python3
"""Implement repeating-key XOR.

Here is the opening stanza of an important work of the English language:

> Burning 'em, if you ain't quick and nimble
> I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first
byte of plaintext will be XOR'd against I, the next C, the next E, then I again
for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your
mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise,
we aren't wasting your time with this.
"""

__author__ = "Joe Ashcraft"
__license__ = "MIT"

import logging
import pprint
from helpers import Candidate
from set1_ch2 import hex_xor

logger = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(width=150, compact=True)

def repeating_key_xor(plaintext:str, key:str) -> str:
    """Encrypt plaintext using repeating-key XOR.

    Args:
        plaintext: str to encrypt
        key: str to use as the key

    Returns:
        (str) the ciphertext in hex
    """
    ciphertext = []
    _plaintext = plaintext.encode('utf-8')
    _key = key.encode('utf-8')
    logging.debug("repeating_key_xor(): plaintext: %s, key: %s", _plaintext, _key)

    for i, byte in enumerate(_plaintext):
        logging.debug("  for( i: %3d,  byte: %3d (%s), key: %s (%s) )", i, byte, chr(byte), _key[i % len(key)], chr(_key[i % len(key)]) )

        ciphertext.append(byte ^ _key[i % len(key)])
        logging.debug("    ciphertext: %s (%s)", ciphertext[-1], hex(ciphertext[-1]))

    return bytes(ciphertext).hex()
    # return ''.join(ciphertext)

def main(puzzle_input_filename:str, key:str):
    """Run each line of puzzle input through repeating_key_xor with the given key. One key per file.

    Returns:
    (list) list of strings, XOR'd from the input file, one string per line.
    """
    _func="main"

    with open(puzzle_input_filename, 'r') as f:
        puzzle_input=f.read().splitlines()
    logger.info(f'{_func}(): read {len(puzzle_input)} lines of puzzle input')


    # run repeating_key_xor for each line of puzzle input
    for line in puzzle_input:
        ciphertext = repeating_key_xor(line, key)
        logging.info("%s -> XOR %s -> %s", line, key, ciphertext)
    return ciphertext

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(main('set1_ch5-input.txt', 'OSWIN'))
