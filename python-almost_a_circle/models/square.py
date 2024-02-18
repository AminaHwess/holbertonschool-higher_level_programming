#!/usr/bin/python3
""" module documentation """

from models.rectangle import Rectangle


class Square(Rectangle):
    """Creating a Class: Square. that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns [Square] (<id>) <x>/<y> - <width>/<height>"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
            )

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def update(self, *args, **kwargs):
        """Assigning an argument to each attribute"""
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)
