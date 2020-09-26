#!/usr/bin/python3
""" add_integer method """


def add_integer(a, b=98):
    """
        add_integer
        this method adds 2 integers

        argments:
            a argument is type int or float
            b argument is type int or float

        raises:
            TypeError: if a or b are not integers or float

        return:
            result of add two integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)