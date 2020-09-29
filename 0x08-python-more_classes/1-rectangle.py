#!/usr/bin/python3
"""
Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """initialization of instance attributes

        Args:
            width (int, optional): Private instance attribute. Defaults to 0.
            height (int, optional): Private instance attribute. Defaults to 0.
        """
        self.__width = width
        self.__height = height


@property
def width(self):
    """getter width

    Returns:
        private: Private instance attribute
    """
    return self.__width


@property
def height(self):
    """getter height

    Returns:
        private: Private instance attribute
    """
    return self.__height


@width.setter
def width(self, value):
    """setter width

    Args:
        value (int): new value

    Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
    """
    if not isinstance(width, int):
        raise TypeError("width must be an integer")
    if width < 0:
        raise ValueError("width must be >= 0")
    self.__width = value


@height.setter
def height(self, value):
    """height setter

    Args:
        value (int): new value

    Raises:
        TypeError: height must be an integer
        ValueError: height must be >= 0
    """
    if not isinstance(height, int):
        raise TypeError("height must be an integer")
    if height < 0:
        raise ValueError("height must be >= 0")
    self.__height = value
