#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return None
    if len(my_list) == 1:
        return my_list[0]
    else:
        if my_list[0] > my_list[1]:
            max = my_list[0]
        else:
            max = my_list[1]
        for i in range(2, len(my_list)):
            if my_list[i] > max:
                max = my_list[i]
    return max
