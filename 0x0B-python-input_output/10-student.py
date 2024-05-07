#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    obj_dict = {}

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        If attrs is a list of strings,
        represents only those attributes
        included in the list
        """
        if type(attrs) == list and
        all(isinstance(attr, str) for attr in attrs):
            for key in attrs:
                if hasattr(self, key):
                    obj_dict[key] = getattr(self, key)
        else:
            obj_dict = self.__dict__.copy()
        return obj_dict
