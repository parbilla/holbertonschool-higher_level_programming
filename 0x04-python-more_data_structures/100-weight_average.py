#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = weight = 0
    for (i, j) in my_list:
            score += (i * j)
            weight += j
    return score / weight
