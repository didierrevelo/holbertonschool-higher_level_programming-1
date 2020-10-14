#!/usr/bin/python3
""" class base for all proyect
"""
import json
from os import path


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

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Writes the string representation of an object of a class
            into a file
        """
        filen = cls.__name__ + ".json"

        list = []
        if list_objs is not None:
            for i in list_objs:
                i = i.to_dictionary()
                json_dict = json.loads(cls.to_json_string(i))
                list.append(json_dict)

        with open(filen, "w") as fd:
            json.dump(list, fd)

