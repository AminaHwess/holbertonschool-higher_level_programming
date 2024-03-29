#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for idx in range(x):
        n += 1
        try:
            print("{}".format(my_list[idx]), end="")
        except IndexError:
            print("")
            return n-1
    print("")
    return n
