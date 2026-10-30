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
import pprint
from helpers import Candidate
from set1_ch3 import main as decryptomator
logger = logging.getLogger(__name__)
pp = pprint.PrettyPrinter(width=150, compact=True)


def main(puzzle_input_filename:str):
    """Run each line of puzzle input through decryptomator, and return the top 3 results by score."""
    _func="main"
    result: list[Candidate] = []

    with open(puzzle_input_filename, 'r') as f:
        puzzle_input=f.read().splitlines()
    logger.info(f'{_func}(): read {len(puzzle_input)} lines of puzzle input')


    # run decryptomator for each line of puzzle input
    for ii, puzzle_line in enumerate(puzzle_input):
        plaintext = decryptomator(puzzle_line) or []
        for key, plain, freq_order, score in plaintext:
            if not plain:
                continue
            candidate = Candidate(
                key=str(key),
                plaintext=str(plain),
                freq_order=str(freq_order),
                score=int(score),
                line=ii,
            )
            result.append(candidate)

    logging.debug("results: %s", result[:-1])

    # print top 3 results by score
    top_results = sorted(result, key=lambda c: c.score, reverse=True)[:3]
    logging.info("%s returns %s", _func, top_results)
    return top_results

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main('set1_ch4-input.txt')
