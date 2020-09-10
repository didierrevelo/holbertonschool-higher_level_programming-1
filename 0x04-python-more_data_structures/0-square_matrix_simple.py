#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if (matrix):
        a = []
        for i in matrix:
            a.append(list(map(lambda x: x ** 2, i)))
        return a
