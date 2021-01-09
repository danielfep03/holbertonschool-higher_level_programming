#!/usr/bin/python3
''' Project for studying doctest in python'''


def matrix_divided(matrix, div):
    '''Function that divides all elements of a matrix'''

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")

    if isinstance(matrix, list) is False or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    for i in range(len(matrix)):
        if isinstance(matrix[i], list) is False or len(matrix[i]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(matrix[i])):
            if isinstance(matrix[i][x], (int, float)) is False:
                raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    new_array = [row[:] for row in matrix]

    for i in range(len(matrix)):
        for x in range(len(matrix[i])):
            new_array[i][x] = round(matrix[i][x] / div, 2)

    return new_array
