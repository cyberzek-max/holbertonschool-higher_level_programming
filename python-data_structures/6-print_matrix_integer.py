#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a=len(matrix)
    b=len(matrix[::])
    for x in range(a):
        for i in range(b):
            if i==b-1:
                print("{:d}".format(matrix[i][x]), end="")
            else:
                print("{:d}".format(matrix[i][x]), end=" ")
        print()
