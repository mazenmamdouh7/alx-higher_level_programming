#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for members in range(len(my_list)):
        if my_list[members] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[members])
    return new_list
