#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_new_list = my_list.copy()
    for idx in range(0, len(my_list)):
        if my_new_list[idx] == search:
            my_new_list[idx] = replace
    return my_new_list
