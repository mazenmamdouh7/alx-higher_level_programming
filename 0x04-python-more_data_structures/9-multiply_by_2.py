#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dirct = {}
    for num in a_dictionary:
        new_dirct = a_dictionary[num] * 2
    return new_dirct
