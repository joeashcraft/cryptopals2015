#!env python3
"""Frequency analysis tools."""
import logging

logger = logging.getLogger(__name__)
from string import ascii_letters, ascii_uppercase, printable, punctuation

ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def letter_counter(message) -> dict:
    """Returns a dictionary with keys of single letters and values of the count of those in the message.

    Case-insensitive! Converts everything to UPPER CASE.
    Ignores anything which is not a letter.

    Today I discovered https://inventwithpython.com/cracking/chapter19.html
    """
    logger.debug(f"letter_counter(message={message[:3]}... {type(message)})")
    if isinstance(message, bytes):
        # decode bytes to ascii string, replace non-ascii with '?'
        logger.info(f"letter_counter() decoding bytes to ascii string")
        _message = message.decode('ascii', errors='replace').upper()
    else:
        _message = message.upper()

    # fmt: off
    _letter_count = {
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,
        "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
        "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
        "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
        "Y": 0, "Z": 0,
    }

    logger.debug(f"letter_counter() message: {_message}")
    for char in _message:
        # logger.debug(f"letter_counter() char: {char} {type(char)}")
        if char in _letter_count:  # avoid punctuation
            _letter_count[char] += 1

    # logger.debug(f"letter_counter() {_letter_count}")
    if max([v for k, v in _letter_count.items()]) > 0:
        logger.debug(f"letter_counter() returns: {_letter_count}")
        return _letter_count
    else:
        logger.debug(f"letter_counter() no letters found")
        return False


def frequency_order(letter_count: dict) -> str:
    """Returns a string sorted by letter frequency, like 'ETAOINSHRDL...'

    Args:
      letter_count: dictionary with keys of UPPER CASE letters and values of integers
    """
    my_list = sorted(letter_count, key=lambda c: letter_count[c], reverse=True)
    my_string = "".join(my_list)
    logger.debug(f"frequency_order() returns: {my_string}")
    return my_string


def freq_scoring(freq_ordered: str) -> int:
    """Returns an integer score of how closely the input matches normal English character frequency distribution ("ETAOIN").

    Scoring algorithm: 1 point for each of the first 6 characters which are
        within the first 6 of ETAOIN, and 1 point for each of the last 6
        characters within the last 6 of ETAOIN. Order within the 6 is not important.
        Ignore the middle 14.

        Special Case: if input exactly matches ETAOIN, then score 100.

    Args:
      input (str): string of upper case characters, representing the frequqncy order of some other plaintext.

    Returns:
      integer score of 0 to 12 (inclusive) or 100
    """
    _func = "freq_scoring"  # function name
    logger.debug(f"{_func}({freq_ordered[:6]}...{freq_ordered[-6:]})")

    if freq_ordered == ETAOIN:
        # just in case the input is perfect, quit early
        logger.debug(f"{_func}() match ETAOIN: 100")
        return 100
    if freq_ordered == ascii_uppercase:
        logger.debug(f"{_func}() match ascii_uppercase: 5")
        # return 5

    score = 0
    for c in freq_ordered[:6]:
        if c in ETAOIN[:6]:
            score += 1
    for c in freq_ordered[-6:]:
        if c in ETAOIN[-6:]:
            score += 1
    logger.debug(f"{_func}() returns: {score}")
    return score
