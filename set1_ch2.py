#!env python3
# Write a function that takes two equal-length buffers and produces their XOR combination.

import sys

def c2(one:bytes, two:bytes):
    """produce hex-encoded XOR of two equal-length hex-encoded strings."""
    assert len(one) == len(two)
    _one=int(one.hex(), 16)
    _two=int(two.hex(), 16)

    return hex(_one ^ _two)


def  hex_xor(one, two):
    """returns byte-encoded XOR result of 2 hex-encoded strings.
    
    compared to c2, this takes hex-encoded strings and returns *bytes*.
    lesson learned from c2: iterating over bytes gives you integer values, so no need for int() if you iterate!
    """
    # hex to bytes
    _a = bytes.fromhex(one)
    _b = bytes.fromhex(two)
    
    # xor bytes
    result = b''
    for b1, b2 in zip(_a, _b):
        result += bytes([b1 ^ b2])
        
    return result


if __name__ == "__main__":
    import sys
    one=sys.argv[1]
    two=sys.argv[2]
    print(f'one={one}')
    print(f'two={two}')
    print(f'result={hex_xor(one,two)}')
