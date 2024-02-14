#!/usr/bin/python3

class Rectangle:

    def display(width, height):

        rec = ""
        for i in range(width):
            rec += '#' * height
        print(rec)
