#!/usr/bin/python3
def uniq_add(my_list=[]):
    n = 0
    uniq = set(my_list)
    for element in uniq:
        n += element
    return n
