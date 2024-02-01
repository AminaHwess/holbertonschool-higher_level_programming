#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_dict = {}
    for key, value in a_dictionary.items():
        updated_dict[key] = value*2
    return updated_dict
