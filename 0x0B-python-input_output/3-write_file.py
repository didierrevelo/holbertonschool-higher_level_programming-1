#!/usr/bin/python3
"""method write a string to a text file"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
