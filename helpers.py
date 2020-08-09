#!env python3

def string_print(s:str):
    """print an ASCII string in
    ascii,
    hex encoded,
    binary"""
    print(f'ascii={s}')
    print('hex=', end='')
    for c in s:
        # print(hex(ord(c))[2:], end='')
        print(c)
    print()
    # print(f'binary=')
