#!/usr/bin/python3
"""
write and create file and print it to stdout
"""


def write_file(filename="", text=""):
    """
    write and create file and print it to stdout
    """
    with open(filename, mode="w+", encoding="UTF8") as f:
        s = f.read()
        f.write(text)
        return len(text)
