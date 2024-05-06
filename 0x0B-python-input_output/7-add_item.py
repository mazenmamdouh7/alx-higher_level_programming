#!/usr/bin/python3
"""This module adds all arguments to a Python list and save them to a file."""
import sys
import json

from 5-save_to_json_file.py import save_to_json_file
from 6-load_from_json_file.py import load_from_json_file

try:
    items = load_from_json_file("add_item.json")
except FileNotFoundError:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, 'add_item.json')
