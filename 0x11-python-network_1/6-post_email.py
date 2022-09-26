#!/usr/bin/python3
"""
task 2 but with requests package
"""


from sys import argv
import requests


if __name__ == '__main__':
    payload = {'email': argv[2]}
    request = requests.post(argv[1], data=payload)

    print(req.text)
