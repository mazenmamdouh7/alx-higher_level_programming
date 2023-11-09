#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for members in sorted(a_dictionary):
        print("{:s}: {}".format(members, a_dictionary[members]))
