#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as url:
        if url.readable():
            Body = url.read()
            print('Body response:')
            print('\t- type: {}'.format(type(Body)))
            print('\t- content: {}'.format(Body))
            print('\t- utf8 content: {}'.format(Body.decode("utf8")))
