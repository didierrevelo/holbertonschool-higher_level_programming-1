#!/usr/bin/python3
""" square """


class Square:
    """ class square empty"""
    def __init__(self, size=0, position=(0, 0)):
        """ initialization of instance attributes
        size (int): the size is an private instance attribute
        """
        self.__size = size
        self.__position = position
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
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """my_print method
        print in stdout a square whit # symbol
        or print "nothing" if size is equal to 0 """
        if self.__size is not 0:
            for i in range(self.position[1]):
                print("")
            for j in range(self.size):
                print(" " * self.position[0], end="")
                for x in range(self.size):
                    print("#", end="")
                print("")
        else:
            print("")

    @property
    def position(self):
        """getter size """
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) is not 2 or\
            type(value[0]) is not int or value[0] < 0 or\
                type(value[1]) is not int or value[1] < 0:
                    raise TypeError("position must be a tuple\
                        of 2 positive integers")
        else:
            self.__position = value
