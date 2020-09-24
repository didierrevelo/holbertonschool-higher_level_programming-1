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
