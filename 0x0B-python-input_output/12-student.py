#!/usr/bin/python3
"""class student
"""


class Student:
    """student class"""
    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json type dict"""
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list) and not (isinstance(attrs[strs], str) for strs in attrs):
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})
