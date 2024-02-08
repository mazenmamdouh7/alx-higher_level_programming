#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for item in a_dictionary:
        print("{}: {}".format(item, a_dictionary[item]*2))
    exit(0)
