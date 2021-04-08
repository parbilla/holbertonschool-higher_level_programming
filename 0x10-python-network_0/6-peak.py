#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):

    list = list_of_integers
    if len(list) < 1:
        return None
    max = list[0]
    if len(list) > 1:
        for i in range(0, (len(list) - 1)):
            if max <= list[i+1]:
                max = list[i+1]
    return max
