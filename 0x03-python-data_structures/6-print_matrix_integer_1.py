#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        var = ' '.join(str(matrix[i][j]) for j in range(len(matrix[i])))
        print(var, end='')
        print()