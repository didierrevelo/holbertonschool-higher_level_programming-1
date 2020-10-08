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


    def to_json(self):
        """json type dict"""
        return self.__dict__
