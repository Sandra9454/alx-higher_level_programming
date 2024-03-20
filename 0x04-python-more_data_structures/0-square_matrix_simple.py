#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix mus be a list of lists")
    return [[element ** 2 for element in row] for row in matrix]
