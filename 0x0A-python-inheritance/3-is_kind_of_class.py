#!/usr/bin/python3
"""is_kind_of_class
    """


def is_kind_of_class(obj, a_class):
    """check if  the object is\
        exactly an instance of\
        the specified class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
