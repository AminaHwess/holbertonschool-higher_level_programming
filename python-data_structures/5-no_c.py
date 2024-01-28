#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for idx in range(0, len(my_string)):
        if my_string[idx] == 'C' or my_string[idx] == 'c':
            continue
        string = string + my_string[idx]
    return string
