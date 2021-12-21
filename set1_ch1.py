#!python
# Convert hex to base64

import base64


def hex_to_b64(s: str):
    bytes_from_hex=bytes.fromhex(s)
    b64_from_bytes=base64.b64encode(bytes_from_hex)
    return b64_from_bytes.decode()

if __name__ == "__main__":
    import sys
    import logging
    hex_string=str(sys.argv[1])
    logging.debug(f'input hex={hex_string}')

    print(hex_to_b64(hex_string))
