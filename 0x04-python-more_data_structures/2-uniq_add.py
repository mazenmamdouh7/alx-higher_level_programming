#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for num in range(len(my_list)):
        if my_list.count(my_list[num]) == 1:
            result += my_list[num]
    return (result)
