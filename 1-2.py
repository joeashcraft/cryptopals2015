#!python
# Write a function that takes two equal-length buffers and produces their XOR combination.

import sys

s1, s2 = sys.argv[1].decode('hex'), sys.argv[2].decode('hex')
#print sys.argv[1].decode('hex').encode('base64')

print ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2)).encode('hex')