#!/usr/bin/python3
def uppercase(str):
    for idx in range(0, len(str)):
        letter = str[idx]
        if ord('a') <= ord(str[idx]) <= ord('z'):
            letter = chr(ord(str[idx]) - 32)
        print("{}".format(letter), end="")
    print()
