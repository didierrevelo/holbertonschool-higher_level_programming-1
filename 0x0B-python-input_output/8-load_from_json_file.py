#!/usr/bin/python3
"""json to python
"""
import json


def load_from_json_file(filename):
    """create an object from json file to python
    """
    with open(filename) as target:
        return json.load(target)
