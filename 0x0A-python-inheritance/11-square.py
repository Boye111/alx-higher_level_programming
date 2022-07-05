#!/usr/bin/python3
"""
Based on the previous tasks
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Rectangle based on square """
    def __init__(self, size):
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
