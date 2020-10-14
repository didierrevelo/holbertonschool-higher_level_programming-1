#!/usr/bin/python3
"""class rectangle"""
from models.base import Base
import sys


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_attributes("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_attributes("y", value)
        self.__y = value

    def area(self):
        """calculate the area
        """
        return self.__width * self.__height

    def display(self):
        """m method
        print in stdout a square whit # symbol
        or print "nothing" if height is equal to 0 """
        for j in range(self.height):
            print("#" * self.width)

    @staticmethod
    def validate_attributes(name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if name is "width" or name is "height":
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def __str__(self):
        """returns string of info about rectangle"""
        return('[Rectangle] ({}) {}/{} - {}/{}'
            .format(self.id, self.x, self.y, self.width, self.height))
