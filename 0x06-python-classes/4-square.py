#!/usr/bin/python3
""" square """


class Square:
    """ class square empty"""
    def __init__(self, size=0):
        """ initialization of instance attributes
        size (int): the size is an private instance attribute
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ area method
        return area square
        """
        return self.__size ** 2

    @property
    def size(self):
        """getter size """
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
