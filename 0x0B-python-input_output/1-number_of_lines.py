#!/usr/bin/python3
"""count number lines"""


def number_of_lines(filename=""):
    """number lines"""
    count = 0
    with open(filename, encoding="utf-8") as f:
        for line in f:
            count += 1
    return count
