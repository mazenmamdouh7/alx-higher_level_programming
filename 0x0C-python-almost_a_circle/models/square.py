#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class."""
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
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns attributes."""
            if args:
                attributes = ['id', 'size', 'x', 'y']
                for attr, value in zip(attributes, args):
                    setattr(self, attr, value)
            else:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)
