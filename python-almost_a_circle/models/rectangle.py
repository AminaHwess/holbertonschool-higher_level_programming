#!/usr/bin/python3
""" module documentation """

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return Rectangle Area"""
        return self.__width * self.__height

    def display(self):
        """Print rectangle instance in stdout"""
        for j in range(self.__y):
            print("")
        for i in range(self.__height):
            x = self.__x * " " + "#" * self.__width
            print(x)

    def __str__(self):
        """Returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """Assigning an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        thisdict = {}
        thisdict["id"] = self.id
        thisdict["width"] = self.__width
        thisdict["height"] = self.__height
        thisdict["x"] = self.__x
        thisdict["y"] = self.__y
        return thisdict
