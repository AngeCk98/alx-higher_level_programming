#!/usr/bin/python3


def square_matrix_simple(matrix=[]):

        result = [list(map((lambda x: x*x), elem)) for elem in matrix]
        return result
