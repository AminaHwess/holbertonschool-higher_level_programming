#!/usr/bin/python3
"""
write and create file and print it to stdout
"""


def append_write(filename="", text=""):
    """
    write and create file and print it to stdout
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        f.write(text)
        return len(text)
