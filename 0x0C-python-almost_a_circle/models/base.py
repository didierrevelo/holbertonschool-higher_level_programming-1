#!/usr/bin/python3
""" class base for all proyect
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns dictionaries"""
        if not list_dictionaries:
            return('[]')
        return(json.dumps(list_dictionaries))
