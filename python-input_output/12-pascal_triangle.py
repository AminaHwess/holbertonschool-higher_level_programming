#!/usr/bin/python3
"""
print pascal's triangle
"""


def pascal_triangle(n):
    """
    print pascal's triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        previous = triangle[-1]
        first = [1]
        for j in range(1, i):
            first.append(previous[j - 1] + previous[j])

        first.append(1)
        triangle.append(first)

    return triangle
