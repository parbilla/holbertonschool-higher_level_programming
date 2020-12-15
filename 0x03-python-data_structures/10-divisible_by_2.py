#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    copy_list = my_list.copy()
    for i in my_list:
        if my_list[i] % 2 == 0:
            copy_list[i] = True
        else:
            copy_list[i] = False
    return copy_list
