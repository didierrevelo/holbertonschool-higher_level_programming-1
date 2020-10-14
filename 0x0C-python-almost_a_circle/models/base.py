#!/usr/bin/python3
""" class base for all proyect
"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializate method"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id