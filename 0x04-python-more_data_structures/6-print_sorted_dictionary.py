#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dictionary = list(a_dictionary)
    sort_dictionary.sort()
    for item in sort_dictionary:
        print("{}: {}".format(item, a_dictionary.get(item)))
    exit(0)
