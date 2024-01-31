#!/usr/bin/python3
def square_value(n):
    return n ** 2


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for idx in range(0, len(new_matrix)):
        new_matrix[idx] = list(map(square_value, new_matrix[idx]))
    return list(new_matrix)
