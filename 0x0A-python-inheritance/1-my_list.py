#!/usr/bin/python3
"""my_list
"""


class MyList(list):
    """[summary]

    Args:
        list (list): inheritance list
    """

    def print_sorted(self):
        print(sorted(self))
