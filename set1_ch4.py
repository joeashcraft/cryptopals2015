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


def xor_and_score(puzzle_input: list[str]) -> list[Candidate]:
    """Run each line of puzzle input through decryptomator, and return the top 3 results by score.

    Returns:
        list[Candidate]: [(key, plaintext, freq_order, score)]
    """
    _func = "xor_and_score"
    result: list[Candidate] = []

    for ii, puzzle_line in enumerate(puzzle_input):
        logging.debug("set1_ch4:%s(): puzzle_line %d: %s", _func, ii, hex(puzzle_line))
        line = str(puzzle_line)
        plaintext = decryptomator(line.rjust(len(line) + len(line) % 2, '0')) or []

        for key, plain, freq_order, score in plaintext:
            if not plain:
                continue
            candidate = Candidate(
                key=str(key),
                plaintext=str(plain),
                freq_order=str(freq_order),
                score=int(score),
                line=ii
            )
            result.append(candidate)

    assert result, "result is empty"
    logging.debug("results: %s", result[:-1])

    top_results = sorted(result, key=lambda c: c.score, reverse=True)[:3]
    assert top_results, "top_results is empty"

    logging.info("set1_ch4:%s() returns %s", _func, top_results)
    return top_results


def main(puzzle_input_filename: str):
    with open(puzzle_input_filename, 'r') as f:
        puzzle_input = f.read().splitlines()
    logger.info('main(): read %s lines of puzzle input', len(puzzle_input))
    return xor_and_score(puzzle_input)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main('set1_ch4-input.txt')
