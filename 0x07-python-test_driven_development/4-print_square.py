#!/usr/bin/python3
"""
prints a square
"""


def print_square(size):
    """ function to print a square in # """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if type(size) is float and size < 0:
        raise TypeError('size must be an integer')

    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print('#', end='')

    if j % size == 0 and j > 0:
        print()
