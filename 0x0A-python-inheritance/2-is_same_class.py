#!/usr/bin/python3
"""
================================
module with method is_same_class
================================
"""


def is_same_class(obj, a_class):
    """Method that return True if an object is an instance of a class"""

    if type(obj) is a_class:
        return True
    else:
        return False
