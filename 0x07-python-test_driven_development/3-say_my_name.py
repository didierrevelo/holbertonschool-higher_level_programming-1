#!/usr/bin/python3
"""
this method print to full name in format
My name is <first name> <last name>
"""
def say_my_name(first_name, last_name=""):
    """say_my_name

    Args:
        first_name ([str]): [first name]
        last_name (str, optional): [last name]. Defaults to "".

    Raises:
        TypeError: [if first name is not str]
        TypeError: [if last name is not str]
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
