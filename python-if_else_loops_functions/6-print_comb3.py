#!/usr/bin/python3
for n in range(0, 10):
    for idx in range(0, 10):
        if n != idx and n*10 + idx < idx*10 + n:
            if ((n*10 + idx != 89) and (idx*10 + n != 89)):
                print("{}{}, ".format(n, idx), end="")
            else:
                print("{}{}".format(n, idx))
