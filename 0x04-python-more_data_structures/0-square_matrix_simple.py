#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sq_matrix[i] = [j**2 for j in matrix[i]]
    return sq_matrix
