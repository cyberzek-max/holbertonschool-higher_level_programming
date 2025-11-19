#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a=len(matrix)
    b=len(matrix[::])
    for i in range(a):
        for x in range(b):
            print("{:d}".format(matrix[i][x]), end=" ")
        print("\n")
