#!/usr/bin/python3
"""append text
"""


def append_write(filename="", text=""):
    """add text at the file
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
