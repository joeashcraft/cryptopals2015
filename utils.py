#!env python3
"""functions that operate on bytes."""
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)


@dataclass
class Ciphertext:
    """A single ciphertext/plaintext with analysis."""

    value: str
    key: str = None
    plaintext: str = None
    freq_order: str = None
    score: int = None
    xor: list = None


def equalize_lengths(a: any, b: any) -> tuple[any, any]:
    """Returns a tuple of two equal length items.

    Args:
        * a (bytes): first bytes object
        * b (bytes): second bytes object
            * if b is a single byte, it will be repeated to match the length of a.
            * if b is more than one byte, it will be repeated to match the length of a.
            * if b is longer than a, it will be truncated to the length of a.


    Never change 'a'.
    """
    logger.debug(f"equalize_lengths(a:{type(a)}={a}, b:{type(b)}={b})")

    if len(b) == 1:
        logger.debug("equalize_lengths():single byte b")
        return (a, b * len(a))  # repeat b to the length of a
    elif len(a) == len(b):
        logger.debug("equalize_lengths():NO OP")
        return (a, b)
    elif len(b) > len(a):
        logger.debug("equalize_lengths():truncating b to the length of a")
        return (a, b[: len(a)])  # truncate b to the length of a
    else:  # 1 < b < a
        logger.debug("equalize_lengths():repeating b to length of a")
        _b = b * (1 + (len(a) // len(b)))  # repeat b to at least the length of a
        return (a, _b[: len(a)])  # truncate b to the length of a


def xor(a: bytes, b: bytes) -> bytes:
    """Returns the XOR result of two bytes objects.

    Args
        * a (bytes): first bytes object
        * b (bytes): second bytes object.

        a and b lengths will be matched using equalize_lengths()

    Returns:
        * bytes: XOR result of the two input bytes objects
    """
    assert all(
        [isinstance(a, bytes), isinstance(b, bytes)]
    ), "a and b must be bytes objects, got %s and %s" % (type(a), type(b))

    (a, b) = equalize_lengths(a, b)

    return bytes([x ^ y for x, y in zip(a, b)])


def single_byte_xor_solve(ciphertext: Ciphertext, count: int = 3) -> tuple:
    """Try to solve a single-byte XOR cipher.

    Args:
        * ciphertext (bytes): the ciphertext to solve
        * count (int): the number of results to return

    Returns:
        (tuple) ((key, plaintext, freq_order, score), ...) sorted by score

    """
    import analysis
    from string import printable

    assert isinstance(ciphertext, bytes), "ciphertext must be bytes"
    assert all(
        [isinstance(count, int), count > 0]
    ), "count must be an integer greater than 0"

    result = dict[
        str:[bytes, str, int]
    ]()  # {'key': [plaintext, freq_order, score], ...}
    # e.g. { 'A': [b'attack at dawn', 'ETAOINSHRDLCUMWFGYPBVKJXQZ', 100] }

    # xor_results = dict[str, bytes]()  # { 'A': b'attack at dawn' }
    # letter_count = dict[str, dict[str, int]]()  # { 'A': { 'A': 1, 'E': 3 } }
    # for k in printable:
    #     xor_results[k] = xor(ciphertext, k.encode())

    # try every printable single-byte key
    for k in printable:
        result[k] = [
            xor(ciphertext, k.encode()),
            "",
            -100,
        ]

    # frequency analysis
    for key, [plaintext, _, score] in result.items():
        result[key] = [plaintext, analysis.letter_counter(plaintext) or {}, score]

    # score the results
    for key, [plaintext, letter_count, score] in result.items():
        if not letter_count:
            logger.info("skip key '%s' because no letters found", key.encode())
            logger.debug("skipped result '%s'", result[key])

            continue
        # determine order of frequency of letters in the plaintext
        logger.debug("key '%s', plaintext '%s'", key.encode(), plaintext)
        freq_ord = analysis.frequency_order(
            letter_count
        )  # e.g. 'ATCDKNWBEFGHIJLMOPQRSUVXYZ'

        # score the plaintext based on the frequency of letters
        score = analysis.freq_scoring(freq_ord, plaintext)  # e.g. 12

        result[key] = [plaintext, freq_ord, score]

    sort_keys = sorted(result, key=lambda k: result[k][2], reverse=True)
    logger.debug("sorted keys: %s", sort_keys)

    # result = (k, [result[k] for k in sort_keys])
    _result = []
    for k in sort_keys:
        _result.append((k, result[k]))
    final_result = tuple(_result)
    # breakpoint()
    logger.info("single_byte_xor_solve: return %s", final_result)
    return final_result[:count]  # TODO rename


def repeating_key_xor(plaintext: bytes, key: bytes) -> bytes:
    """Encrypt plaintext using repeating-key XOR.
    If key is 'ICE', then 'ICEICEICE...' will be used.

    Args:
        plaintext (bytes): the plaintext to encrypt
        key (bytes): the key

    Returns:
        (bytes) the result
    """
    ciphertext = []
    logging.debug("repeating_key_xor(): plaintext: %s, key: %s", plaintext, key)

    for i, byte in enumerate(plaintext):
        logging.debug(
            "  for( i: %3d,  byte: %3d (%s), key: %s (%s) )",
            i,
            byte,
            chr(byte),
            key[i % len(key)],
            chr(key[i % len(key)]),
        )

        ciphertext.append(byte ^ key[i % len(key)])
        logging.debug("    ciphertext: %s (%s)", ciphertext[-1], hex(ciphertext[-1]))

    logger.info("repeating_key_xor() returns %s bytes", len(ciphertext))
    return bytes(ciphertext)
