#!/usr/bin/python3
"""
Class to JSON
"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data structure"""
    return obj.__dict__
