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

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
