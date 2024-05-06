#!/usr/bin/python3
"""This module defines a Python class-to-JSON function."""
import json


def class_to_json(obj):
    """function that returns the dictionary description with simple 
    data structure (list, dictionary, string, integer and boolean)
    for JSON serialization of an object."""
    return json.dumps(obj)
