#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        a_dictionary = sorted(a_dictionary.items(), key=lambda x: x[1], \
                              reverse=True)
        res = next(iter(a_dictionary))
        return res[0]
    else:
        return None
