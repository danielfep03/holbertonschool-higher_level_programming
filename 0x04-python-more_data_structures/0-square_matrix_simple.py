#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for sublist in matrix:
        new_matrix.append(list(map(lambda n: n ** 2, sublist)))
    return new_matrix
