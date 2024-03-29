#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle class  """

    def __init__(self, width=0, height=0):
        """initialization of instance attributes
        Args:
                        width (int, optional): Private\
                                instance attribute. Defaults to 0.
                        height (int, optional): Private\
                                instance attribute. Defaults to 0.
        """
        self.width = width
        self.height = height

    def area(self):
        """ area method
        return area square
        """
        return self.__width * self.__height

    def perimeter(self):
        """perimeter

        Returns:
                perimeter: returns the add of sides
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    @property
    def width(self):
        """getter width
        Returns:
        private: Private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """"setter width
                        Args:
        value (int): new value

Raises:
        TypeError: width must be an integer
        ValueError: width must be >= 0
"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height

        Returns:
                        private: Private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
                        value (int): new value

        Raises:
                        TypeError: height must be an integer
                        ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __str__(self):
        """str method
        Returns:
            int: [description]
        """
        new = ""
        if self.__width == 0 or self.__height == 0:
            return new
        for i in range(self.__height):
            for j in range(self.__width):
                new = new + "#"
            new = new + '\n'
        return new[:-1]

    def __repr__(self):
        """repr method

        Returns:
            repr: string represantation
        """
        new = ""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del method
        """
        print("Bye rectangle...")
