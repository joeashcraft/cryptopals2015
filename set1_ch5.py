#!/usr/bin/env python3
"""Implement repeating-key XOR.

Here is the opening stanza of an important work of the English language:

> Burning 'em, if you ain't quick and nimble
> I go crazy when I hear a cymbal

Encrypt it, under the key "ICE", using repeating-key XOR.

In repeating-key XOR, you'll sequentially apply each byte of the key; the first
byte of plaintext will be XOR'd against I, the next C, the next E, then I again
for the 4th byte, and so on.

It should come out to:

0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your
mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise,
we aren't wasting your time with this.

USAGE: python3 set1_ch5.py [<plaintext_file> <key_file>]

With no args, encrypts the challenge stanza under key ICE.
With two args, both files are read as ASCII (key trailing newline stripped).
"""

__author__ = "Joe Ashcraft"
__license__ = "MIT"

import logging
import sys
import utils
from string import printable

logger = logging.getLogger(__name__)

CHALLENGE_PLAINTEXT = (
    "Burning 'em, if you ain't quick and nimble\n" "I go crazy when I hear a cymbal"
)
CHALLENGE_KEY = "ICE"


def main(plaintext: str, key: str) -> bytes:
    """Encrypt ASCII plaintext with repeating-key XOR.

    Returns:
        (bytes) ciphertext
    """
    # if plaintext is hex-only, use bytes.fromhex()
    try:
        _plaintext = bytes.fromhex("".join(plaintext.split()))
        logger.warning("plaintext is hex")
    except ValueError:
        _plaintext = plaintext.encode("utf-8")
    _key = key.encode("utf-8")

    ciphertext = utils.repeating_key_xor(_plaintext, _key)
    logger.info("%r -> XOR %r -> %s", plaintext, key, ciphertext.hex())
    return ciphertext


if __name__ == "__main__":  # pragma: no cover
    logging.basicConfig(level=logging.ERROR)

    if len(sys.argv) not in (1, 3):
        print("USAGE: python3 set1_ch5.py [<plaintext_file> <key_file>]")
        sys.exit(1)

    if len(sys.argv) == 1:
        plaintext, key = CHALLENGE_PLAINTEXT, CHALLENGE_KEY
    else:
        with open(sys.argv[1], "r") as f:
            plaintext = f.read()
        with open(sys.argv[2], "r") as f:
            key = f.read().rstrip("\n")

    result = main(plaintext, key)

    print(
        "==> hex <==\n%s" % result.hex(),
        "==> UTF-8 <==\n%s" % result.decode(encoding="utf-8"),
        sep="\n\n",
        end="",
    )
