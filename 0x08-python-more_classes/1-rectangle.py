#!/usr/bin/python3
"""
A simple Rectangle
"""


class Rectangle:
    """ a class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        self.check_width(width)
        self.check_height(height)

        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.check_width(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.check_height(value)
        self.__height = value

    def check_width(self, width):
        if self.check_if_int(width) is False:
            raise TypeError('width must be an integer')
        if self.check_if_positive(width) is False:
            raise ValueError('width must be >= 0')

    def check_height(self, height):
        if self.check_if_int(height) is False:
            raise TypeError('height must be an integer')
        if self.check_if_positive(height) is False:
            raise ValueError('height must be >= 0')

    def check_if_int(self, value):
        if type(value) is int:
            return True
        return False

    def check_if_positive(self, value):
        if value >= 0:
            return True
        return False
