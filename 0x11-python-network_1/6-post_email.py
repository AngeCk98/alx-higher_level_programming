#!/usr/bin/python3
"""
Script that sends a POST request to URL with email as a parameter
and displays the body of the response
"""

import requests as req
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    address = sys.argv[2]
    r = req.post(url, data={'email': address})
    print(r.text)
