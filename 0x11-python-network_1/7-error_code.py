#!/usr/bin/python3
"""
using request package to do task 3
"""


from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])

    if request.status_code >= 400:
        print('Error code:', request.status_code)
    else:
        print(request.text)
