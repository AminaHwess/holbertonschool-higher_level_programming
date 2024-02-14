#!/usr/bin/python3
"""
Creating a first class : base.
"""


class base:
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
            base.__nb_objects += 1
            self.id = base.__nb_objects
