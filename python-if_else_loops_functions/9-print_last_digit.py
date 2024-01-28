#!/usr/bin/python3
def print_last_digit(number):
    if abs(number) > 9:
        lastdigit = abs(number) % 10
    elif 0 <= abs(number) <= 9:
        lastdigit = abs(number)
    print(lastdigit, end="")
    return lastdigit
