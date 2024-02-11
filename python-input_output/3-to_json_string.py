#!/usr/bin/python3
"""
return JSON representation of object
"""


def to_json_string(my_obj):
    """
    return JSON representation of my_obj
    """
    import json

    return json.dumps(my_obj)
