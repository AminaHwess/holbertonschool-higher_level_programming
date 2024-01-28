#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx in range(0, len(matrix)):
        for n in range(0,  len(matrix[idx])):
            print("{:d}".format(matrix[idx][n]), end="")
            if n < len(matrix[idx])-1:
                print(end=" ")
        print()
