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
        super().__init__(size, size)

    def __str__(self):
        return f"[{str(self.__class__.__name__)}] \
{str(self.__size)}/{str(self.__size)}"
