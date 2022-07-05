#!/usr/bin/python3
"""
Write to a filebto a text string
"""


def write_file(filename="", text=""):
    """ Function that writes a string to a text file """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
