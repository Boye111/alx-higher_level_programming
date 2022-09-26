#!/usr/bin/python3
"""
task one but only using requests package
"""


from sys import argv
import requests


if __name__ == "__main__":
    request = requests.get(argv[1])

    print(request.headers.get('X-Request-Id'))
