#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == 0:
        tuple = (None, 0)
    else:
        tuple = (len(sentence), sentence[0])
    return tuple
