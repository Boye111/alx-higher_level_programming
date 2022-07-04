#!/usr/bin/python3
"""
A function that return True or False
"""


def inherits_from(obj, a_class):
    """ inherits from some """
    if isinstance(obj, a_class) and \
            issubclass(a_class, obj.__class__) is False:
        return True

    return False
