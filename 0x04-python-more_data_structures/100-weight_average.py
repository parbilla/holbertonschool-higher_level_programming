#!/usr/bin/python3
def weight_average(my_list=[]):
    score = weight = 0
    for (i, j) in my_list:
            score += (i * j)
            weight += j
    return score / weight
