#!/usr/bin/python3
"""
class Rectangle that inherts
"""


from models.base import Base


class Rectangle(Base):
    """ rectangle that inherits """

    def __init__(self, width, height, x=0, y=0, id=None):
        """  super class with id """
        super().__init__(id)

        self.check_integer_parameter(width, 'width')
        self.check_integer_parameter(height, 'height')
        self.check_integer_parameter(x, 'x')
        self.check_integer_parameter(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ define width """
        return self.__width

    @width.setter
    def width(self, param):
        """ define width """
        self.check_integer_parameter(param, 'width')

        self.__width = param

    @property
    def height(self):
        """ define height """
        return self.__height

    @height.setter
    def height(self, param):
        """ define height """
        self.check_integer_parameter(param, 'height')

        self.__height = param

    @property
    def x(self):
        """ definition of x """
        return self.__x

    @x.setter
    def x(self, param):
        """ definition of x """
        self.check_integer_parameter(param, 'x')

        self.__x = param

    @property
    def y(self):
        """ definition of y """
        return self.__y

    @y.setter
    def y(self, param):
        """ definition of y """
        self.check_integer_parameter(param, 'y')

        self.__y = param

    def check_integer_parameter(self, value, param):
        """ check integer parameter """
        if type(value) is not int:
            raise TypeError(param + ' must be an integer')

        if value <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if value < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def area(self):
        """ arear of rectangle """
        return self.__width * self.__height

    def display(self):
        """ display of rectangle """
        if self.__y > 0:
            print('\n' * self.__y, end='')

        for i in range(self.height):
            if self.__x > 0:
                print(' ' * self.__x, end='')

            print('#' * self.__width)

    def __str__(self):
        """ definition of str """
        return '[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}'.format(
                self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ updating the class """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ dictionary of class """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
