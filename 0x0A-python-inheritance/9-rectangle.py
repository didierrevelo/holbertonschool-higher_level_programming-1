#!/usr/bin/python3
"""BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle

    Args:
        BaseGeometry (class): inheritance
    """
    def __init__(self, width, height):
        """initialization"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """calculate the area
        """
        return self.__width * self.__height

    def __str__(self):
        """str
        """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
