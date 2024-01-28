#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    old_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    elif 0 <= idx <= len(my_list) - 1:
        old_list[idx] = element
    return old_list
