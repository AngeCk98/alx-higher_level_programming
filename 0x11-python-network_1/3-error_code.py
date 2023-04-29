#!/usr/bin/python3
"""
Script to manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""

from urllib.request import Request, urlopen
import sys
from urllib.error import HTTPError


if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urlopen(url) as response:
            print(response.read().decode('utf8'))
    except HTTPError as e:
        if hasattr(e, 'code'):
            print('Error code:', e.code)
