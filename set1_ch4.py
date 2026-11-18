#!/usr/bin/env python3
"""Detect single-character XOR.

One of the 60-character strings in
[this file](https://cryptopals.com/static/challenge-data/4.txt) has been
encrypted by single-character XOR.

Find it.

(Your code from #3 should help.)
"""

__author__ = "Joe Ashcraft"
__license__ = "MIT"

import logging
import utils

logger = logging.getLogger(__name__)


def main(puzzle_input_filename: str):
    with open(puzzle_input_filename, 'r') as f:
        puzzle_input = f.read().splitlines()
    logger.info('main(): read %s lines of puzzle input', len(puzzle_input))
    # for line in puzzle_input:
    # do utils.single_byte_xor_solve() for each line
    # return the top 3 results by score
    top_results = []
    for line in puzzle_input:
        results = utils.single_byte_xor_solve(bytes.fromhex(line))
        top_results.append(results[0])  # best 1 result

    return sorted(top_results, key=lambda x: x[1][2], reverse=True)[
        :3
    ]  # best 3 results


if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.ERROR)

    print(main("set1_ch4-input.txt"))
