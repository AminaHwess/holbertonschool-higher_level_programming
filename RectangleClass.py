#!/usr/bin/python3
Base = __import__("Base.py").Base

class Rectangle(Base):
        print_symbol = "#"
        def __init__(self, width=0, height=0):
            self.__height = height
            self.__width = width

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

        
        def area(self):
            """
            Return Rectangle area
            """
            return self.__height * self.__width
        
        def display(self):

            rec = ""
            for i in range(self.__width):
                rec += '#' * self.__height
            print(rec)

        def update(self, *args):
