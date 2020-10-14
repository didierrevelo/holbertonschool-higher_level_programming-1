#!/usr/bin/python3
"""square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Inherits from:
            Rectangle
            Base
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
            Overwritting the ste method
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """assigns arguments"""
        if args:
            keys = ["id", "size", "x", "y"]
            for key, value in zip(keys, args):
                setattr(self, key, value)
        else:
            keys = ["id", "size", "x", "y"]
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        dict = {}
        key = ['id',
               'width',
               'height',
               'x',
               'y']

        for i in key:
            dict[i] = getattr(self, i)
        return dict