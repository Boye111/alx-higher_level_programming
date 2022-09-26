#!/usr/bin/python3
"""
Body and errors
"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError


if __name__ == "__main__":
    r = Request(argv[1])

    try:
        with urlopen(r) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as ex:
        print('Error code:', ex.code)
