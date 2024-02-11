#!/usr/bin/python3

"""
turn class obj into JSON str rep
"""
import json


def class_to_json(obj):
    """
    turn class obj into JSON string rep
    """

    return obj.__dict__
