#!/usr/bin/python3

"""
check if object is instance of class
"""


def inherits_from(obj, a_class):
    """
    check if object is instance of class
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
