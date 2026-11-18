#!env python3
"""presentation functions."""

import utils


def string_print(s: str):  # pragma: no cover
    """print an ASCII string in
    ascii,
    ascii to hex-encoded string,
    binary"""
    print(f"ascii={s}")
    print(f"hex={ascii_to_hex(s)}")
    print(f"binary={ascii_to_binary(s)}")


##
## from ascii
##
def ascii_to_hex(input: str) -> str:
    """returns hex-encoded string from ascii string input

    lessons learned over string_to_hex():
    - discovered bytes.hex()
    """
    return input.encode().hex()


def ascii_to_binary(input: str) -> str:
    """returns binary string from ascii string input."""
    return " ".join(f"{b:08b}" for b in input.encode())


##
## from bytes
##
def bytes_to_binary(data: bytes) -> str:
    """returns binary string from bytes input."""
    return " ".join(f"{b:08b}" for b in data)


##
## from hex
##
def hex_string_to_ascii_string(s: str):
    if s[:2] == "0x":
        s = s[2:]
    return bytes.fromhex(s).decode()


def hex_to_b64(s: str):
    """returns base64-encoded string from hex-encoded string.

    input: hex-encoded string, e.g. 'DEADBEEF'
    return: (str) base64-encoded string, e.g. '3q2+7w=='
    """
    import base64

    bytes_from_hex = bytes.fromhex(s)
    b64_from_bytes = base64.b64encode(bytes_from_hex)
    return b64_from_bytes.decode()


def hex_xor(one: str, two: str) -> bytes:
    """returns byte-encoded XOR result of 2 equal-length hex-encoded strings.

    input:
        * one (str): hex-encoded string, e.g. 'DEADBEEF'
        * two (str): hex-encoded string, e.g. 'FACEFEED'
    return: (bytes) XOR result of the two input strings
    """
    assert len(one) == len(two), "input strings must be of equal length"
    _a = bytes.fromhex(one)
    _b = bytes.fromhex(two)

    return utils.xor(_a, _b)


if __name__ == "__main__":  # pragma: no cover
    print('## string_print("abc") ##')
    string_print("abc")
    print()

    print('## ascii_to_hex("abc") ##')
    print(ascii_to_hex("abc"))
