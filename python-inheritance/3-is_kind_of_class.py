#!/usr/bin/python3
"""
check if obj is instance of class
"""


def is_kind_of_class(obj, a_class):
    """
    check if obj is instance of class
    """
    if isinstance(obj, a_class) or type(obj) is a_class:
        return True
    else:
        return False
