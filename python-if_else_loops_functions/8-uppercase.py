#!/usr/bin/python3
def uppercase(str):
    for idx in range(0, len(str)):
        if ord('a') <= ord(str[idx]) <= ord('z'):
            print("{}".format(chr(ord(str[idx]) - 32)), end="")
        else:
            print("{}".format(str[idx]), end="")
