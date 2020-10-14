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
    def size(self, val):
        """
            setter
        """
        self.validate_attributes("width", val)
        self.width = val
        self.height = val

    def __str__(self):
        """
            Overwritting the ste method
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
