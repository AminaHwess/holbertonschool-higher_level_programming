#!/usr/bin/python3
"""
Creating a first class : base.
"""


class Base:
    """
    Class : base.
    """

    __nb_objects = 0
    """
    Private class attribute
    """

    def __init__(self, id=None):
        """
        Class constructor.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
