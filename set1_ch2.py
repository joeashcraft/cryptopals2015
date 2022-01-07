#!env python3
# Write a function that takes two equal-length buffers and produces their XOR combination.

import sys

def c2(one:str, two:str):
    """produce hex-encoded XOR of two equal-length hex-encoded strings."""
    assert len(one) == len(two)
    _one=int(one.hex(), 16)
    _two=int(two.hex(), 16)

    return hex(_one ^ _two)

if __name__ == "__main__":
    import sys
    one=sys.argv[1]
    two=sys.argv[2]
    print(f'one={one}')
    print(f'two={two}')
    print(f'result={c2(one,two)}')
