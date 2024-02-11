#!/usr/bin/python3

"""
Class Square that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square that inherits from Rectangle
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        self.area(self)
        super().__init__(size, size)
