#!env python3
"""functions that operate on bytes."""
import logging
logger = logging.getLogger(__name__)


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
