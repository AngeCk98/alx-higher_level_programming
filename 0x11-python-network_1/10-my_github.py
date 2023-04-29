#!/usr/bin/python3
"""
Script to display Github id using OAuth
"""

import requests as req
import sys

if __name__ == "__main__":
    response = req.get('https://api.github.com/user', auth=(
             sys.argv[1], sys.argv[2]))
    res = response.json()
    print(res.get("id"))
