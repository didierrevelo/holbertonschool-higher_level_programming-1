#!/usr/bin/python3
"""read file
"""


def read_lines(filename="", nb_lines=0):
    """read line and print only lines
    """
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines >= count:
            print(f.read(), end='')
        else:
            for line in range(nb_lines):
                print(f.readline(), end='')
