#!/usr/bin/python3
"""
Empty class that defines a rectangle
"""


class Rectangle:
    """
    class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return (self._Rectangle__height + self._Rectangle__width) * 2

    def __str__(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return ""
        for i in range(self._Rectangle__height):
            for j in range(self._Rectangle__width):
                print("#", end="")
            if i != self._Rectangle__height - 1:
                print("")
        return ""

    def __repr__(self):
        return f"Rectangle({self._Rectangle__height}, \
{self._Rectangle__width})"
