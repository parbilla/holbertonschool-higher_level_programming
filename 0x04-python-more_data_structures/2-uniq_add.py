#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_list = []
    for i in range(len(my_list)):
        if my_list[i] not in uni_list:
            uni_list.append(my_list[i])
    return sum(uni_list)
