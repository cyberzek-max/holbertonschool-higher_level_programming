#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a=len(matrix)
    b=len(matrix[::])
    for i in range(a):
        for x in range(b):
            if x==b-1:
                print("{:d}".format(matrix[i][x]), end=" ")
            else:
                print("{:d}".format(matrix[i][x]), end="")
        print("\n")
