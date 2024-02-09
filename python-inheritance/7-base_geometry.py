#!/usr/bin/python3


"""
raise exception
"""


class BaseGeometry:
    """
    raise exception
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(value, int) and isinstance(name, str):
            raise TypeError(f"{name} must be an integer")
        if value <= 0 and isinstance(name, str):
            raise ValueError(f"{name} must be greater than 0")
