#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmat = [[ el**2 for el in row ] for row in matrix ]
    return newmat
