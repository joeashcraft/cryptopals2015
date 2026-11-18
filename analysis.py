#!env python3
"""Frequency analysis tools."""
import logging

logger = logging.getLogger(__name__)
from string import ascii_letters, ascii_uppercase, printable, punctuation

ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
ZQXJKV = "ZQXJKVBPYGFWMUCLDRHSNIOATE"  # opposite of ETAOIN


def letter_counter(message) -> [dict, bool]:
    """Returns False or a dictionary with keys of single letters and values of the count of those in the message.

    Case-insensitive! Converts everything to UPPER CASE.
    Ignores anything which is not a letter.

    Today I discovered https://inventwithpython.com/cracking/chapter19.html
    """
    logger.debug(f"letter_counter(message={message[:3]}... {type(message)})")
    if isinstance(message, bytes):
        # decode bytes to ascii string, replace non-ascii with '?'
        logger.debug(f"letter_counter() decoding bytes to ascii string")
        _message = message.decode("ascii", errors="replace").upper()
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
    assert isinstance(
        letter_count, dict
    ), "analysis.frequency_order expect dict, got %s" % type(letter_count)
    logger.debug("frequency_order(letter_count=%s)", letter_count)

    my_list = sorted(letter_count, key=lambda c: letter_count[c], reverse=True)
    for c in ZQXJKV:
        # for letters not present, final order should match ZQXJKV
        if letter_count[c] == 0:
            my_list.remove(c)
            my_list.append(c)

    my_string = "".join(my_list)
    logger.debug("frequency_order() returns: %s", my_string)
    return my_string


def freq_scoring(freq_ordered: str, plaintext: str = None) -> int:
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

    score = 0
    for common_letter in freq_ordered[:6]:
        if common_letter in ETAOIN[:6]:
            score += 1
        if common_letter in ETAOIN[-6:]:
            score -= 1
    for uncommon_letter in freq_ordered[-6:]:
        if uncommon_letter in ETAOIN[-6:]:
            score += 1
        if uncommon_letter in ETAOIN[:6]:
            score -= 1

    if plaintext:
        logger.debug("%s() plaintext='%s'", _func, plaintext)
        for c in plaintext:
            if not chr(c) in printable:
                logger.debug("{_func}() plaintext byte '%s' not printable", (c))
                score -= 1

    logger.debug(f"{_func}() returns: {score}")
    return score


def hamming_distance(string_a: bytes, string_b: bytes) -> int:  # set1_ch6
    """returns the bit-level Hamming distance between two strings."""
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

    diff_pointer = ""
    for bit1, bit2 in zip(_string_a, _string_b):
        if bit1 != bit2:
            diff_pointer += "^"
        else:
            diff_pointer += " "
    logging.debug("set1_ch6:hamming_distance(): string_a    : %s", _string_a)
    logging.debug("set1_ch6:hamming_distance(): string_b    : %s", _string_b)
    logging.debug("set1_ch6:hamming_distance(): diff_pointer: %s", diff_pointer)
    logging.debug(
        "set1_ch6:hamming_distance() returns: %d",
        sum(bit1 != bit2 for bit1, bit2 in zip(_string_a, _string_b)),
    )

    return sum(bit1 != bit2 for bit1, bit2 in zip(_string_a, _string_b))
