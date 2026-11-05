#!env python3
""" presentation functions."""

from dataclasses import dataclass
import utils


@dataclass(frozen=True)
class Candidate:
    key: str
    plaintext: str
    freq_order: str
    score: int
    line: int = -1

    def __post_init__(self):
        assert isinstance(self.key, str) and self.key, "key must be a non-empty str"
        assert isinstance(self.plaintext, str) and self.plaintext, "plaintext must be a non-empty str"
        assert isinstance(self.freq_order, str) and self.freq_order, "freq_order must be a non-empty str"
        assert isinstance(self.score, int), "score must be an int"
        assert isinstance(self.line, int), "line must be an int"


def string_print(s:str):
    """print an ASCII string in
    ascii,
    ascii to hex-encoded string,
    binary"""
    print(f'ascii={s}')
    print(f'hex={string_to_hex(s)}')
    print(f'binary={ascii_to_binary(s)}')

def string_to_hex(s:str):
    """returns hex-encoded string from ascii string input, but slowly.

    deprecated by ascii_to_hex()
    """
    # hex_encoded_string='0x'
    hex_encoded_string=''
    for c in s:
        hex_encoded_string+=hex(ord(c))[2:]
    return hex_encoded_string

def ascii_to_hex(input:str) -> str:
    """returns hex-encoded string from ascii string input

    lessons learned over string_to_hex():
    - discovered bytes.hex()
    """
    return input.encode().hex()

def ascii_to_binary(input:str) -> str:
    """returns binary string from ascii string input. """
    return " ".join(f"{b:08b}" for b in input.encode())

def bytes_to_binary(data: bytes) -> str:
    """returns binary string from bytes input. """
    return " ".join(f"{b:08b}" for b in data)

##
## from hex
##
def hex_string_to_ascii_string(s:str):
    if s[:2]=='0x':
        s=s[2:]
    return bytes.fromhex(s)

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


if __name__ == "__main__":
  print('## string_print("abc") ##')
  string_print('abc')
  print()

  print('## string_to_hex("abc") ##')
  print(string_to_hex('abc'))
