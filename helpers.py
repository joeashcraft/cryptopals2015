#!env python3

from dataclasses import dataclass


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
    print()
    # print(f'binary=')

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

def hex_string_to_ascii_string(s:str):
    if s[:2]=='0x':
        s=s[2:]
    return bytes.fromhex(s)


if __name__ == "__main__":
  print('## string_print("abc") ##')
  string_print('abc')
  print()

  print('## string_to_hex("abc") ##')
  print(string_to_hex('abc'))
