#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    a = len(matrix)
    b = len(matrix[::])
    for x in range(a):
        for i in range(len(matrix[x])):
            if i == len(matrix[x])-1:
                print("{:d}".format(matrix[x][i]), end="")
            else:
                print("{:d}".format(matrix[x][i]), end=" ")
        print()
