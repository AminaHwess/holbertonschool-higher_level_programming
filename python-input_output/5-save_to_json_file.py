#!/usr/bin/python3

"""
function that writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, JSON rep
    """
    import json

    with open(filename, "w") as file:
        json.dump(my_obj, file)
