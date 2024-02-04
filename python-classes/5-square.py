#!/usr/bin/python3
"""
Empty Square with private instance 'size'
"""


class Square:
    """
    Empty square.
    """

    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):

        """
        Empty Square with private instance 'size'.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self._Square__size = value

    def area(self):
        """
        Returns square area.
        """
        return self._Square__size**2

    def my_print(self):
        """
        prints square.
        """
        if self._Square__size == 0:
            print()
        else:
            for i in range(0,  self._Square__size):
                for j in range(0, self._Square__size):
                    print('#', end="")
                print()
