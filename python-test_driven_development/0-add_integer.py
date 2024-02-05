#!/usr/bin/python3
""""
Code that returns an addition of two integers
"""


def add_integer(a, b=98):
    """
    Function to return the sum of two integer values.
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return a + b
