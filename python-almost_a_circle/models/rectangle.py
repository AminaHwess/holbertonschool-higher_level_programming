#!/usr/bin/python3

from models.base import base


class Rectangle(base):

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

        @width.setter
        def width(self, value):
            if isinstance(value, int) and value >= 0:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if isinstance(value, int) and value >= 0:
                self.__height = value
