#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = max(a_dictionary.values(), default=None)
    for a, b in a_dictionary.items():
        if b == highest:
            return a
