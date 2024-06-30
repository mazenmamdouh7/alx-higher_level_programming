#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number to be added, must be an integer or a float.
        b: The second number to be added, must be an integer or a float (default is 98).

    Returns:
        The integer addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
