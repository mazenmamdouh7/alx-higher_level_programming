#!/usr/bin/python3
"""Define an empty class Rectangle."""


class Rectangle:
    """Class that define a properties of rectangle."""
    def __init__(self, width=0, height=0):
        """Intialize a new rectangle.

        Args:
            Width(int): the width of the rectangle.
            height(int): the height of the rectangle.
        """
        slef.width = width
        self.height = height
    
    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter the width of the rectangle.

        Args:
            value(int): the width value to be set.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(vlaue, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value
    
    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter the height of the rectangle.

        Args:
            value(int): the width value to be set.

        Raises:
            TypeError: if the value is not an integer.
            ValueError: if the value is less than 0.
        """
        if not isinstance(vlaue, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
