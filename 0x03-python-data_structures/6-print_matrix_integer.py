#!/usr/bin/python4
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1 and len(matrix[0]) == 0:
        print("")
    else:
       for i in matrix:
        for j in i:
            if j != i[-1]:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j))
    exit(0)
