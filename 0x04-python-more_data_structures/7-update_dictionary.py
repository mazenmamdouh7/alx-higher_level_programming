#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary.update({key: value})
    for item in a_dictionary:
        print("{}: {}".format(item, a_dictionary[item]))
    exit(0)
