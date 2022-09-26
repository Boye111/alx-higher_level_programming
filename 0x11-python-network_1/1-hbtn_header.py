#!/usr/bin/python3
"""
sends request to get content found in the header
"""


from sys import argv
from urllib.request import Request, urlopen


if __name__ = "__main__":
    request = Request(argv[1])

    with urlopen(request) as res:
        headers = res.info()
        print(headers.get('X-Request-Id'))
