#!/usr/bin/python3

"""
return an object represented by a JSON string
"""


def from_json_string(my_str):
    """
    return an object represented by a JSON string
    """
    import json

    return json.loads(my_str)
