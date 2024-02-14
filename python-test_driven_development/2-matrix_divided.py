#!/usr/bin/python3
"""
Divide Matrix by div
"""


def matrix_divided(matrix, div):
    """
    Divides each element of the given matrix by the provided number.
    """

    for lis in matrix:
        for i in lis:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
        if len(matrix[0]) != len(lis):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for idx in range(len(matrix)):
        new_matrix.append(list(map(lambda x: round(x / div, 2), (matrix[idx]))))
    return new_matrix
