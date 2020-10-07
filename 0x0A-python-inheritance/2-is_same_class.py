#!/usr/bin/python3
"""is_same_class
    """


def is_same_class(obj, a_class):
    """[summary]

    Args:
        obj (instance)
        a_class

    Returns:
        [type]: return true is intance of a_class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
