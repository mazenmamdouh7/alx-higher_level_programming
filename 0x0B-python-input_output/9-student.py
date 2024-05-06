#!/usr/bin/python3
"""This module defines a class student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Function that retrieves a dictionary
        representation of a Student instance."""
        return Student.__dict__
