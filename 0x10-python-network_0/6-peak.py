#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):

    list = list_of_integers
    max = 0
    if len(list) < 3:
        return None
    if len(list) == 3:
        return list[2]
    for i in range(1, (len(list) - 2)):
        if list[i] < list[i+1]:
            max = list[i+1]
    return max
