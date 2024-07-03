#!/usr/bin/python3
"""Module for Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """A square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """method that return
        [Square] (<id>) <x>/<y> - <size>
        """
        return ("""[Square] ({}) {}/{} - {}"""
                .format(self.id, self.x, self.y, self.height))
