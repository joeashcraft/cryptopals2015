#!python
# Single-byte XOR cipher
# The hex encoded string:
#  1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# ... has been XOR'd against a single character.
# Find the key, decrypt the message.
#
# You can do this by hand. But don't: write code to do it for you.
#
# How? Devise some method for "scoring" a piece of English plaintext.
# Character frequency is a good metric. Evaluate each output and
# choose the one with the best score.


import sys
import logging
logger = logging.getLogger(__name__)

from string import ascii_letters, ascii_uppercase, printable, punctuation
from helpers import hex_xor, hex_string_to_ascii_string
from analysis import letter_counter, frequency_order, freq_scoring
from utils import equalize_lengths, xor

def main(input:str) -> list:
    """given PUZZLE INPUT, return the most likely KEY and PLAINTEXT.

    Cipher algorithm is XOR with a repeated ASCII character.

    ARGS:
      input: the PUZZLE INPUT, a hex-encoded string
    RETURN:
      (list) sorted list of tuples containing the KEY, PLAINTEXT, FREQ_ORDER_STR, SCORE, sorted by SCORE
    """
    logger.debug("set1_ch3:main(input=%s)", input)
    HEAD = 1  # how many results to print

    # convert input to bytes
    input = bytes.fromhex(input)
    logger.debug(f"set1_ch3:main(): input={input}")

    # calculate the XOR result for every possible single-byte key
    xor_results = {k: xor(input, k.encode()) for k in "bX"}
    logger.debug("xor_results=%s", xor_results)

    # frequency analysis
    letter_count = dict[
        str, dict[str, int]
    ]()  # dict of dicts like { KEY: {'A': 1, 'E': 3}, 'b': {'A':0, 'B':0, 'E':3}}
    for result_key, result_plaintext in xor_results.items():
        try:
            letter_count[result_key] = letter_counter(result_plaintext)
        except ValueError as e:
            continue  # no letters found for key

    # score the results
    result = (
        list()
    )  # e.g. [('A', 'Attack at Dawn', 'ATCKDWN', 12), ('B', 'Bttbck bt Dbwn', 'BTCKDWN' 1)]
    for k,v in letter_count.items():
        if not v:
            logger.info("skip key '%s' because no letters found", k.encode())
            continue
        freq_ord = frequency_order(v)  # e.g. 'OZWETAQ...'
        score = freq_scoring(freq_ord)
        # reduce score for each character not printable
        for c in xor_results[k]:
            if chr(c) not in printable:
                logger.debug("score -2 for non-printable character '%s'", chr(c))
                score-=2
            if chr(c) in punctuation:
                logger.debug("score -1 for punctuation character '%s'", chr(c))
                score-=1
            if chr(c) in " ":  # required characters
                score += 1
        result.append((k, xor_results[k], freq_ord, score))

    # logger.debug(f'unsorted result: {result[:2]}')
    result.sort(key=lambda x: x[3], reverse=True)
    # logger.debug(f'sorted result: {result[:2]}')

    # print top HEAD results
    logger.debug("set1_ch3:main() returns %s ..." % result[:HEAD])
    return result[:HEAD]


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    input, key = None, None
    if not len(sys.argv)>1:
        input='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        # key='X'
    else:
        input=sys.argv[1]
        key=sys.argv[2]

    print(f"set1_ch3: input={input}")
    print(f"set1_ch3: key={key}")

    result = main(input)
    print(
        "key is probably '%s' (%s)\nmessage '%s'"
        % (result[0][0], result[0][0].encode(), result[0][1].decode())
    )
