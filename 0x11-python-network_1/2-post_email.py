#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == "__main__":
    data = urlencode({'email': argv[2]}).encode('ascii')
    request = Request(argv[1], data)

    with urlopen(request) as res:
        print(res.read().decode('utf-8'))
