#!/usr/bin/python3
"""save to json file
"""


def save_to_json_file(my_obj, filename):
    """json file
    """
    import json
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
