#!/usr/bin/python3
"""returns the JSON representation
"""


def to_json_string(my_obj):
    """returns the JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
