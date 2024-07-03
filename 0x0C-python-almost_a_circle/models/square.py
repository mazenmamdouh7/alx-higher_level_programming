#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method should return
        [Square] (<id>) <x>/<y> - <size>
        """
        return ("""[Square] ({}) {}/{} - {}"""
                .format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """Size of this square"""
        return self.width, self.height

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
