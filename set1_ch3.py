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
from string import ascii_letters, ascii_uppercase, printable, punctuation
from set1_ch2 import c2 as hex_xor

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def main(input:str) -> list:
    """given PUZZLE INPUT, return the most likely KEY and PLAINTEXT.

    Cipher algorithm is XOR with a repeated ASCII character.

    ARGS:
      input: the PUZZLE INPUT, a hex-encoded string
    RETURN:
      (list) sorted list of tuples containing the KEY, PLAINTEXT, FREQ_ORDER_STR, SCORE, sorted by SCORE
    """
    logging.debug("main() called with input=%s", input)
    HEAD=3 # how many results to print
    result=list()  # e.g. [('A', 'Attack at Dawn', 'ATCKDWN', 12), ('B', 'Bttbck bt Dbwn', 'BTCKDWN' 1)]
    letter_count=dict()  # dict of dicts like { KEY: {'A': 1, 'E': 3}, 'b': {'A':0, 'B':0, 'E':3}}

    results = c3(input, None)
    for result_key,result_plaintext in results.items():
        letter_count[result_key]=letter_counter(result_plaintext)
    # logging.debug(f"X: {letter_count['X']}")

    for k,v in letter_count.items():
        freq_ord = frequency_order(v)  # e.g. 'OZWETAQ...'
        score = freq_scoring(freq_ord)
        # reduce score for each character not printable
        for c in results[k]:
            if c not in printable:
                score-=2
            if c in punctuation:
                score-=1
            if c in ' ':  # required characters
              score+=1
        result.append(
            (k, results[k], freq_ord, score)
        )

    # logging.debug(f'unsorted result: {result[:2]}')
    result.sort(key=lambda x: x[3], reverse=True)
    # logging.debug(f'sorted result: {result[:2]}')

    logging.debug("main() returns %s " % result[:HEAD])
    return(result)




def letter_counter(message:str)->dict:
    """Returns a dictionary with keys of single letters and values of the count of those in the message.

    Case-insensitive! Converts everything to UPPER CASE.
    Ignores anything which is not a letter.

    Today I discovered https://inventwithpython.com/cracking/chapter19.html
    """
    _message=message.upper()
    _letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0,
                     'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                     'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0,
                     'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for char in _message:
        if char in _letter_count:  # avoid punctuation
            _letter_count[char]+=1
    return _letter_count


def frequency_order(letter_count:dict)->str:
    """Returns a string sorted by letter frequency, like 'ETAOINSHRDL...'

    Args:
      letter_count: dictionary with keys of UPPER CASE letters and values of integers
    """
    my_list=sorted(letter_count, key=lambda c: letter_count[c], reverse=True)
    my_string=''.join(my_list)
    return my_string


def freq_scoring(freq_ordered:str)->int:
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
    _func="freq_scoring"  # function name
    logging.debug(f"{_func}({freq_ordered[:6]}...{freq_ordered[-6:]})")

    if freq_ordered == ETAOIN:
        # just in case the input is perfect, quit early
        return 100

    score=0
    for c in freq_ordered[:6]:
        if c in ETAOIN[:6]:
            score+=1
    for c in freq_ordered[-6:]:
        if c in ETAOIN[-6:]:
            score+=1
    return score

def equalize_lengths(a, b) -> tuple:
    """Returns a tuple of two equal length items.

    Never change 'a'.
    """
    logging.debug(f"equalize_lengths(a:{type(a)}={a}, b:{type(b)}={b})")
    if len(a) != len(b) and len(b)==1:
        """intended use case."""
        logging.debug("equalize_lengths() a and b differ in len")
        return (a, b*len(a))
    elif len(a) == len(b):
        logging.debug("equalize_lengths() no op, return the inputs unmodified")
        return (a, b)
    # else:
    #     """ignore all but first character of b."""
    #     return (a, str(b)[0]*len(a))

def c3(input:str, key:str):
    """Returns dict of {key: plaintext, ...}.

    If no key given, try every ascii_letter.

    ARGS:
        input: a hex-encoded string (e.g. 'deadbeef')
        key: ascii-string
    """
    logging.debug(f'c3(input={input}, key={key})')
    _input=None
    _key=None
    result=dict()

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
        try:
            string_result = bytes_result.decode()  # e.g. "Cooking MC's like a pound of bacon"
        except UnicodeDecodeError:
            return {key: False}
        result[key]=string_result
        return result

    else:
    # if no key given, try every printable
        for k in printable:
            logging.debug(f'trying key {k}')
            _key = k.encode()  # such as b'X'
            # _key:str=hex(ord(k))[2:]  # such as '0x7a'

            _input, _key = equalize_lengths(_input, _key)
            h_e_s=hex_xor(_input, _key)[2:]
            # h_e_s=hex_xor(input, key*len(_input))[2:]
            logging.debug(f'hex result={h_e_s}')
            try:
                ascii_string=helpers.hex_string_to_ascii_string(h_e_s).decode('utf-8')
                result[k]=ascii_string
                logging.info(f'{k}: {result[k]}')
            except ValueError:
                logging.debug('hex result does not translate to ascii')
    # >>> bytes.fromhex(str(hex(int(_input.hex(),16) ^ int(_key.hex(),16))[2:]))
    # b"Cooking MC's like a pound of bacon"
        return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    input, key = None, None
    if not len(sys.argv)>1:
        input='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        # key='X'
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
    main(input)
