#!/usr/bin/python3
"""
Integer Addition
"""


def add_integer(a, b=98):
    """ Function to add two numbers """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    a = convert_to_int(a)
    b = convert_to_int(b)
    return a + b

def convert_to_int(num):
    """ Convert to int """
    if type(num) is float:
        num = int(num)
        return num

    return num
