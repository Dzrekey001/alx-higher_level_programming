#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    keys = list(a_dictionary.keys())
    keys.sort()
    return (keys[-1])
