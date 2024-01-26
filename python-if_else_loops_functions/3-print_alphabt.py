#!/usr/bin/python3
for idx in range(ord('a'), ord('z')+1):
    if (idx != 101) and (idx != 113):
        print("{}".format(chr(idx)), end="")
