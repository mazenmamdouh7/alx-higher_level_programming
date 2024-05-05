#!/usr/bin/python3
"""This module defines a text file-reading function."""


def read_file(filename=""):
    """Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: The name of file wanted to read.
    """
    with open(filename, 'r', encoding= 'utf-8') as file:
        data = file.read()
        print(data)
