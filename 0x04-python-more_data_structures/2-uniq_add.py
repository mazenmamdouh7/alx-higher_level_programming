#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniqe_values = set(my_list)
    SumOfUniqe = 0
    for values in uniqe_values:
        SumOfUniqe += values
    return SumOfUniqe
