#!/usr/bin/python3
"""This module defines a text file-writing function."""

def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) 
    and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fw:
        return fw.write(text)

