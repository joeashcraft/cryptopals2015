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
import utils

logger = logging.getLogger(__name__)

if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.ERROR)

    input, key = None, None
    if not len(sys.argv) > 1:
        input = bytes.fromhex(
            "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
        )
        # key='X'
    else:
        input = sys.argv[1]
        key = sys.argv[2]

    print(f"set1_ch3: input={input}")
    print(f"set1_ch3: key={key}")

    # result = main(input)
    results = utils.single_byte_xor_solve(input, 3)

    print("key: message")
    for result in results:
        print(result)
        # print("%s (%s): '%s'" % (result[0], result[0].encode(), result[1][0].decode()))
