#!/usr/bin/python3
for idx in range(0, 100):
    if (0 <= idx <= 98):
        print("{:02d}{}".format(idx, ", "), end="")
    if (idx == 99):
        print("{:02d}".format(idx))
