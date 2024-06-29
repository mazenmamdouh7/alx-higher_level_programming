#!/usr/bin/python3
"""This module defines a json to object function."""
import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)
    represented by a JSON string."""
    return json.loads(my_str)