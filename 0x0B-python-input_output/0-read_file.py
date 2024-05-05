#!/usr/bin/python3

def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout.

    Args:
        filename: the Name of the file.
    Returns:
        The input of the file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
