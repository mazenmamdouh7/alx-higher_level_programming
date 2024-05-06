#!/usr/bin/pyhton3
"""This module defines a string-to-JSON function."""
import json

def to_json_string(my_obj):
    """Function returns the JSON representation of an object (string)."""
    return json.dumps(my_obj)
