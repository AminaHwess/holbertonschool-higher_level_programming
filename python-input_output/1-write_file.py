#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(text)
    return len(text)
