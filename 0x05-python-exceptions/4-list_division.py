#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    New_List = []
    for item in range(0, list_length):
        try:
            div = (my_list_1[item]/my_list_2[item])
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            New_List.append(div)
    return New_List
