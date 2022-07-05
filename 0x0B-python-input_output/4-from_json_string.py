#!/usr/bin/python3
"""
From JSON string to Object
"""


from json import loads


def from_json_string(my_str):
    """a function that returns an object"""
    return loads(my_str)
