#!/usr/bin/python3
"""
Body and errors
"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    request = Request(argv[1])

    try:
        with urlopen(result) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code:', ex.code)
