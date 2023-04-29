#!/usr/bin/python3
"""
Script to check first 10 commits to a Github repo
"""

import requests as req
import sys

if __name__ == "__main__":
    url = req.get('https://api.github.com/repos/{}/{}/commits'
                  .format(sys.argv[2], sys.argv[1]))

    r = url.json()
    for c in r[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
