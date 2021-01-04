#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        n_dict = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
        res = next(iter(n_dict))
        return res[0]
    else:
        return None
