#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        c = my_list[0]
        for idx in range(0, len(my_list)):
            if c < my_list[idx]:
                c = my_list[idx]
        return c
