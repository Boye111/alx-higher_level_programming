#!/usr/bin/python3
"""
A class that inherits from list
"""


class MyList(list):
    """ prints list in asc """
    def print_sorted(self):
        if issubclass(MyList, list):
            print(sorted(self))
