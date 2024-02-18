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
            self.id, self.x, self.y, self.height
            )

    @property
    def size(self):
        return self.__height
