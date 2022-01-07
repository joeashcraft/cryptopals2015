#!env python3

def string_print(s:str):
    """print an ASCII string in
    ascii,
    ascii to hex-encoded string,
    binary"""
    print(f'ascii={s}')
    print(f'hex={string_to_hex(s)}')
    print()
    # print(f'binary=')

def string_to_hex(s:str):
    # hex_encoded_string='0x'
    hex_encoded_string=''
    for c in s:
        hex_encoded_string+=hex(ord(c))[2:]
    return hex_encoded_string
    
def hex_string_to_ascii_string(s:str):
    if s[:2]=='0x':
        s=s[2:]
    return bytes.fromhex(s)


if __name__ == "__main__":
  print('## string_print("abc") ##')
  string_print('abc')
  print()
  
  print('## string_to_hex("abc") ##')
  print(string_to_hex('abc'))