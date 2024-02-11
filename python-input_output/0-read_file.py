#!/usr/bin/python3
"""
read file and print it to stdout
"""


def read_file(filename=""):
    """
    read text file (UTF8) and print it to stdout
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        s = f.read()
        print(s, end="")
