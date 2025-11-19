#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = list(map(lambda x : x**2, matrix[::][::]))
    return newmat
