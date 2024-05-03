#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    if type(obj) is not a_class and  isinstance(obj, a_class):
        return True
    else:
        return False
