#!/usr/bin/python3
"""BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry
    """
    def area(self):
        """area

        Raises:
            Exception: that raises an Exception\
            with the message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator
        Raises:
            TypeError: raise a TypeError exception,\
                with the message <name> must be an integer
            ValueError: raise a ValueError exception\
                with the message <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
