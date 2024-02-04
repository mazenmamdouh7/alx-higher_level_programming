#!/usr/bin/python4
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:
            if j != i[-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
    exit(0)
