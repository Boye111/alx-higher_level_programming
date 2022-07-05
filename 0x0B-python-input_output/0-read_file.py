#!/usr/bin/python3
"""
Documentation about 0x0B
"""


def read_file(filename=""):
    """Task 1 of the above operation"""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            print(line, end='')
