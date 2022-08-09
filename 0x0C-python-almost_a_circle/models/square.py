#!/usr/bin/python3
"""
......
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """ A square that is a subclass of a rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ definition of class constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ string in class """
        return '[Square] ({:d}) {:d}/{:d} - {:d}'.format(
                self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """ size of value in class """
        return self.width

    @size.setter
    def size(self, value):
        """ size of value in class """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updating the class """
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """ dictionary to class """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
