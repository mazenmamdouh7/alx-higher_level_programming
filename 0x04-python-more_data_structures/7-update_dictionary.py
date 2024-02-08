#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for member in a_dictionary:
            if member == key:
                a_dictionary[member] = value
    return a_dictionary
