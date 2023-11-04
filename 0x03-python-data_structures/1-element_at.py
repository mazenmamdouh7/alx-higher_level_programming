#!/usr/bin/python3
def element_at(my_list, idx):
    long_of_list = len(my_list) - 1 
    if (idx < 0 or idx > long_of_list):
        return(None)
    else:
        return(my_list[idx])
