#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        _max = max(a_dictionary.values())
        return [key for key, i in a_dictionary.items() if i == _max][0]
