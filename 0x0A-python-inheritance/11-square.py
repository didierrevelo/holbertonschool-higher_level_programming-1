#!/usr/bin/python3
"""
    implementing a Geometry class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class inherited from Rectangle
    """
    def __init__(self, size):
        """initialization
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area
        """
        return (self.__size ** 2)

    def __str__(self):
        """str
        """
        return ("[Square] {}/{}".format(self.__size, self.__size))
