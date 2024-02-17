#!/usr/bin/python3
"""Defines class Rectangle  (based on 0-rectangle.py)"""


class Rectangle:
    """Class that defines properties of rectangle.

    Attributes:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
    """
    def __init__(self, width=0, height=0):
        """Creates new instances of Rectangle.
        
        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        """width retriver.
        
        Returns:
        int: the width of the rectangle.
        """
        return self.__width
    
    @property
    def height(self):
        """Height retriver.
        
        Returns:
        int: the height of the rectangle.
        """
        return self.__height
    
    @width.setter
    def width(self, value):
        """Property setter for width of the rectangle.
        
         Args:
            value (int): width of the rectangle.

        Raise:
            TypeError: If the width is not an integer.
            valueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value
    
    @height.setter
    def height(self, value):
        """Property setter for height of the rectangle.
        
         Args:
            value (int): height of the rectangle.

        Raise:
            TypeError: If the height is not an integer.
            valueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
