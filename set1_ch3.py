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
from string import ascii_letters
from s1_c2 import c2 as hex_xor

def c3(input:str, key:str):
    # assert len(input) == len(key)
    _input=bytes.fromhex(input)
    ret=''
    for c in _input:
         ret+=hex(c^ord(key))[2:]
    return ret

    # return hex_xor(input, 'b'*len(input))
    # for c in ascii_letters:
    #     print hex_xor(input, c*len(input))


if __name__ == "__main__":
    import sys
    input=sys.argv[1]
    key=sys.argv[2]

    print(f'input={input}')
    print(f'key={key}')
    print(f'result={c3(input, key)}')
