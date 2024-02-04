#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        d = a/b
    except ZeroDivisionError:
        d = None
    finally:
        print("{}: {}".format('Inside Result', d))
        return d
