#!/usr/bin/python3
""" add_integer method

    this method adds 2 integers

"""


def add_integer(a, b=98):
    """add_integer this method adds 2 integers
        argments:
            a argument is type int or float
            b argument is type int or float
        return:
            result of add two integers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
