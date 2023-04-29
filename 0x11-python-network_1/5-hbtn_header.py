#!/usr/bin/python3
"""
Script that displays the value of the variable
X-Request-Id in the response header
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    r = response.headers.get('X-Request-Id')
    print(r)
