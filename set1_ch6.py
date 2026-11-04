#!/usr/bin/env python3

"""(the puzzle input has) been base64'd after being encrypted with repeating-key XOR.

Decrypt it.

Here's how:

1. Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
2. Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
        `this is a test`
    and
        `wokka wokka!!!`
    is 37. Make sure your code agrees before you proceed.
3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
7. Solve each block as if it was single-character XOR. You already have code to do this.
8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
"""

__author__ = "Joe Ashcraft"
__license__ = "MIT"

import logging
import base64
from helpers import ascii_to_binary
from set1_ch4 import xor_and_score
logger = logging.getLogger(__name__)


def hamming_distance(string_a:bytes, string_b:bytes) -> int:
    """returns the bit-level Hamming distance between two strings. """
    # 2. Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
    #         `this is a test`
    #     and
    #         `wokka wokka!!!`
    #     is 37. Make sure your code agrees before you proceed.

    _string_a = string_a
    _string_b = string_b
    # ensure input is bytes
    if type(_string_a) != bytes:
        _string_a = ascii_to_binary(_string_a)
    if type(_string_b) != bytes:
        _string_b = ascii_to_binary(_string_b)

    diff_pointer=''
    for bit1, bit2 in zip(_string_a, _string_b):
        if bit1 != bit2:
            diff_pointer += '^'
        else:
            diff_pointer += ' '
    logging.debug("set1_ch6:hamming_distance(): string_a    : %s", _string_a)
    logging.debug("set1_ch6:hamming_distance(): string_b    : %s", _string_b)
    logging.debug("set1_ch6:hamming_distance(): diff_pointer: %s", diff_pointer)
    logging.debug("set1_ch6:hamming_distance() returns: %d", sum(bit1 != bit2 for bit1, bit2 in zip(_string_a, _string_b)))

    return sum(bit1 != bit2 for bit1, bit2 in zip(_string_a, _string_b))

def guess_keysize(puzzle_input:bytes, key_size_max:int=40, best_guesses:int=3)->list[list[int, float]]:
    # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    # 4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
    logging.debug("set1_ch6:guess_keysize() called with: key_size_max: %s, best_guesses: %s", key_size_max, best_guesses)

    guesses=[] # [[key_size, hamming_distance_normalized]]
    for ii in range(1, key_size_max+1):
        hamming_distance_normalized = hamming_distance(puzzle_input[:ii], puzzle_input[ii:2*ii]) / ii
        logging.debug("  try key_size: %s, hamming_distance_normalized: %s", ii, hamming_distance_normalized)

        guesses.append([ii, hamming_distance_normalized])
        # logging.info("guess_keysize(): best key_size: %s (%.2f)", key_size[0], key_size[1])

    top_guesses = sorted(guesses, key=lambda x: x[1])[:best_guesses]
    logging.info("set1_ch6:guess_keysize() returns: %s", top_guesses)
    return top_guesses


def blocks_by_keysize(ciphertext: bytes, keysize: int) -> list[bytes]:
    # 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
    result = []
    for i in range(0, len(ciphertext), keysize):
        result.append(ciphertext[i:i+keysize])
    logging.debug("set1_ch6:blocks_by_keysize() returns: %s", result)
    return result

def transpose_blocks(blocks: list[bytes]) -> list[bytes]:
    # 6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
    result = []
    for i in range(0, len(blocks[0])):
        column = []
        for j in range(len(blocks)):
            try:
                column.append(blocks[j][i])
            except IndexError:
                column.append(0)
        # logging.debug("transpose_blocks() column: %s", column)
        result.append(bytes(column))
    logging.debug("set1_ch6:transpose_blocks() returns: %s", result)
    return result

# 7. Solve each block as if it was single-character XOR. You already have code to do this.
# 8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.


def main(puzzle_input_filename:str, key_size_max:int=40):
    result = []

    with open(puzzle_input_filename, 'r') as file:
        puzzle_input_b64 = file.read().strip() # str

    puzzle_input = base64.b64decode(puzzle_input_b64) # bytes

    # 3. For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
    # 4. The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
    possible_keysizes = guess_keysize(puzzle_input, key_size_max=5, best_guesses=3)

    for ii in possible_keysizes:
        logging.debug("set1_ch6:main(): trying keysize: %s", ii[0])
        # 5. Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
        blocks = blocks_by_keysize(puzzle_input, keysize=ii[0]) # [b'abc', b'def', b'ghi', b'jkl']

        # 6. Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
        blocks = transpose_blocks(blocks) # [b'adgj', b'behk', b'cfil']

        for block in blocks:
            # # ensure all blocks are equal length, fill with 0
            # if not len(block) == len(blocks[0]):
            #     logging.debug("  found uneven block length, padding with 0: %s", block)
            #     block = block.ljust(len(blocks[0]), '0')

            # block=bytes(block)
            logging.debug("set1_ch6:main():  block: %s (%d)", block, len(block)/2)

            # 7. Solve each block as if it was single-character XOR. You already have code to do this.
            scored = xor_and_score(block) # [('0', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5), ('1', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5), ('2', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 5), ...]
            logging.info("set1_ch6:main(): scored: %s", scored)

            # 8. For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
            block_key = min(scored, key=lambda x: x[3])[0]
            logging.info("set1_ch6:main(): block_key: %s", block_key)
            result.append(block_key)
    return result

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    print(main(puzzle_input_filename='set1_ch6-input.txt', key_size_max=8))


