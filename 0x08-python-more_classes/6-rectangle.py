#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.
       
       Args:
          number_of_instances(int): The number of Rectangle instance.
    """

    number_of_instances = 0

    def _init_(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The width value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The height value to be set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self._width * self._height

    def perimeter(self):
        """Calculate and return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return 0
        return 2 * (self._width + self._height)

    def _str_(self):
        """Return a printable representation of the Rectangle.

        The rectangle is represented using the '#' character.
        """
        if self._width == 0 or self._height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            rect.extend(["#"] * self.__width)
            if i != self.__height - 1:
                rect.append("\n")
        return "".join(rect)

    def _repr_(self):
        """Return the string representation of the Rectangle.

        The representation is in the form: Rectangle(width, height)
        """
        return f"Rectangle({self._width}, {self._height})"

    def _del_(self):
        """print a message after deleting a rectangle object and update the number of instance."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
