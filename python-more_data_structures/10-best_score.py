#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        for keys, values in a_dictionary.items():
            if values == max(a_dictionary.values()):
                return keys
