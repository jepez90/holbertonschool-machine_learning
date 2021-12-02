#!/usr/bin/env python3
"""
    Function that adds two matrices:

    You can assume that mat1 and mat2 are matrices containing ints/floats
    You can assume all elements in the same dimension are of t same type/shape
    You must return a new matrix
    If matrices are not the same shape, return None
    You can assume that mat1 and mat2 will never be empty
"""


def add_matrices(mat1, mat2):
    """ adds two matrices """

    # check if the lists can be added
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    sum_mat = []

    # if the list contains more lists
    if type(mat1[0]) is list:
        # for each sublist in the current list
        for i in range(len(mat1)):
            # append of response of the recursive call of the function
            sum_mat.append(add_matrices(mat1[i], mat2[i]))

    # if the list contains numbers
    else:

        # add the numbers in the lists
        for i in range(len(mat1)):
            sum_mat.append(mat1[i] + mat2[i])

    return sum_mat


def matrix_shape(matrix):
    """ calculates the shape of a matrix: """
    if type(matrix) is list:
        response = [len(matrix)]
        response.extend(matrix_shape(matrix[0]))
        return response
    return []
