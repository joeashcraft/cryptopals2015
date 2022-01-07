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
import helpers
from string import ascii_letters
from set1_ch2 import c2 as hex_xor


def main(input:str) -> list:
    """given PUZZLE INPUT, return the most likely KEY and PLAINTEXT.
    
    Cipher algorithm is XOR with a repeated ASCII character.
    
    ARGS:
      input: the PUZZLE INPUT, a hex-encoded string
    RETURN:
      (list) sorted list of tuples containing the KEY and possible PLAINTEXTS, sorted by best guess at real English
    """
    pass

def equalize_lengths(a, b) -> tuple:
    """Returns a tuple of two equal length items.
    
    Never change 'a'.
    """
    logging.debug(f"equalize_lengths(a:{type(a)}={a}, b:{type(b)}={b})")
    if len(a) != len(b) and len(b)==1:
        """intended use case."""
        return (a, b*len(a))
    elif len(a) == len(b):
        logging.debug("equalize_lengths() no op, return the inputs unmodified")
        return (a, b)
    # else:
    #     """ignore all but first character of b."""
    #     return (a, str(b)[0]*len(a))

def c3(input:str, key:str):
    """
    ARGS:
        input: a hex-encoded string (e.g. 'deadbeef')
        key: ascii-string
    """
    logging.debug(f'c3(input={input}, key={key})')
    _input=None
    _key=None

    _input=bytes.fromhex(input)
    logging.debug(f'bytes input={_input}')



    if key:
    # if key given, convert to raw bytes
        # _key=bytes.fromhex(helpers.string_to_hex(key))
        _key=key.encode()

    # if len(_key) != len(_input):
    # if key given, make it the same length as input
        # _key = _key * len(_input)
        # logging.debug(f'new key={_key}')
        _input, _key = equalize_lengths(_input, _key)
        logging.debug(f'bytes key={_key}')
    # elif len(_key) == len(_input):
    #     _key=key
    #     logging.debug(f'new key={_key}')
    
    # ret=''
    # for c in _input:
    #      ret+=hex(c^ord(key))[2:]
    # return ret

        assert isinstance(_input, bytes)        
        assert isinstance(_key, bytes)
        hex_result = hex_xor(_input, _key)  # e.g. 0x436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e
        hex_encoded_string_result = str(hex_result)[2:]  # e.g. '436f6f6b696e67204d432773206c696b65206120706f756e64206f66206261636f6e'
        bytes_result = bytes.fromhex(hex_encoded_string_result)  # e.g. b"Cooking MC's like a pound of bacon"
        string_result = bytes_result.decode()  # e.g. "Cooking MC's like a pound of bacon"
        
        return string_result

    else:  #if not key
    # if no key given, try every ascii_letters
        for k in ascii_letters:
            logging.debug(f'trying key {k}')
            _key:str=hex(ord(k))[2:]  # such as '0x7a'

            _input, _key = equalize_lengths(_input, _key)
            h_e_s=hex_xor(_input, _key)[2:]
            # h_e_s=hex_xor(input, key*len(_input))[2:]
            logging.debug(f'hex result={h_e_s}')
            try:
                ascii_string=helpers.hex_string_to_ascii_string(h_e_s).decode('utf-8')
            except ValueError:
                logging.debug('hex result does not translate to ascii')
            print(f'is this even English? {ascii_string}')
    # >>> bytes.fromhex(str(hex(int(_input.hex(),16) ^ int(_key.hex(),16))[2:]))
    # b"Cooking MC's like a pound of bacon"
        return


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    if not len(sys.argv)>1:
        input='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        key='X'
    else:
        input=sys.argv[1]
        key=sys.argv[2]

    # >>> format(0x1b, '#010b')
    # '0b00011011'
    # >>> format(ord('X'), '#010b')
    # '0b01011000'
    # >>> format(ord('C'), '#010b')
    # '0b01000011'
    
    # >>> chr(ord('X') ^ int('1b',16))
    # 'C'


    print(f'input={input}')
    print(f'key={key}')
    print(f'result={c3(input, key)}')
