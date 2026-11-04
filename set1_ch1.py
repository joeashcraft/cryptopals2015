#!python
# Convert hex to base64

from helpers import hex_to_b64


if __name__ == "__main__":
    import sys
    import logging
    logging.basicConfig(level=logging.DEBUG)

    try:
        hex_string=str(sys.argv[1])
    except IndexError:
        hex_string='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    logging.debug('set1_ch1:hex_string=%s', hex_string)

    print(hex_to_b64(hex_string))
