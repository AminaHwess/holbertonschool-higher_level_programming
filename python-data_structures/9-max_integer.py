#!/usr/bin/python3
def max_integer(my_list=[]):
    c = my_list[0]
    if my_list is None:
        return None
    else:
        for idx in range(0, len(my_list) - 2):
            if c < my_list[idx + 1]:
                c = my_list[idx + 1]
            return c
