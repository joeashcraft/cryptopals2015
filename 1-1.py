#!python
# Convert hex to base64

import sys

print sys.argv[1].decode('hex').encode('base64')