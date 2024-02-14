#!/usr/bin/python3
"""
Class : Rectangle
"""

from models.base import base

"""
Create class Rectangle that inherits from Base
"""


class Rectangle(base):
    """
    Class Rectangle
    Set private instance attributes
    SetClass constructor
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__height = height
        self.__width = width
        self.__x = x
        self.__y = y

        @property
        def x(self):
            return self.__x

        @property
        def y(self):
            return self.__y

        @property
        def width(self):
            return self.__width

        @property
        def height(self):
            return self.__height

        @width.setter
        def width(self, value):
            if isinstance(value, int) and value >= 0:
                self.__width = value

        @height.setter
        def height(self, value):
            if isinstance(value, int) and value >= 0:
                self.__height = value

        @x.setter
        def X(self, value):
            if isinstance(value, int) and value >= 0:
                self.__x = value

        @y.setter
        def X(self, value):
            if isinstance(value, int) and value >= 0:
                self.__y = value
