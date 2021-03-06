#!/usr/bin/python3
"""
A simple REctangle
"""


class Rectangle:
    """ A class that defines a rectangle """
    def __init__(self, width=0, height=0):
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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
