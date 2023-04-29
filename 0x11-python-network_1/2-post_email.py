#!/usr/bin/python3
"""
Script to pass parameter to header
"""

import urllib.request
from urllib.request import urlopen as lop
from urllib.parse import urlencode as enc
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    address = sys.argv[2]
    values = {"email": address}
    data = enc(values)
    data = data.encode('utf8')
    req = urllib.request.Request(url, data)
    with lop(req) as response:
        print(response.read().decode('utf8'))
