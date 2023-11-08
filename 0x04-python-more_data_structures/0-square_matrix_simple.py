#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[s ** 2 for s in r] for r in matrix]
    return  new_matrix
