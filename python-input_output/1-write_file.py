#!/usr/bin/python3
"""
append text to file
"""
def append_write(filename="", text=""):
    """
    append text to file
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        f.read(text)
        return len(text)
