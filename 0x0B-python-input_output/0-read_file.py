#!/usr/bin/python3
"""read file
"""


def read_file(filename=""):
    """read file
    """
    with open('my_file_0.txt', 'r') as f:
        print(f.read())
