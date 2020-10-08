#!/usr/bin/python3
""" class MyInt"""


class MyInt(int):
    """inherited from int"""
    def __init__(self, num):
        self.num = num

    def __ne__(self, value):
        return self.num == value

    def __eq__(self, value):
        return self.num != value
