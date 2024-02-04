#!/usr/bin/python3
"""
Empty Square with private instance 'size'
"""


class Square:
    """
    Empty square.
    """

    def __init__(self, size=0):
        """
        Empty Square with private instance 'size'.
        """
        self._Square__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        pass
