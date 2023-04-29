#!/usr/bin/python3
"""
Script to display value of 'X-Request-Id' variable from URL header
"""

from urllib.request import urlopen
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    with urlopen(url) as response:
        headers = response.info()
        print(response.headers['X-Request-Id'])
