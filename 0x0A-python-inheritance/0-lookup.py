#!/usr/bin/python3
"""lookup
"""


def lookup(obj):
    """type search

    Args:
        obj (class): class

    Returns:
        list or dir : list or dir of types of obj
    """
    return dir(obj)
