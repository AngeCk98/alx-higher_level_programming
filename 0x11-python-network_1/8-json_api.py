#!/usr/bin/python3
"""
Script that sends a POST request variable sent as
argument and checks if body of response is JSON valid
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sq = {"q": ""}
    else:
        sq = {"q": sys.argv[1]}

    res = requests.post('http://0.0.0.0:5000/search_user', data=sq)

    try:
        result = res.json()
        if result == {}:
            print('No result')
        else:
            print('[{}] {}'.format(result["id"], result["name"]))
    except ValueError:
        print('Not a valid JSON')
