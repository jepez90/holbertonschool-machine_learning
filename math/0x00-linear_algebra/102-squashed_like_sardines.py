#!/usr/bin/env python3
"""
    Function that concatenates two matrices along a specific axis:

    You can assume that mat1 and mat2 are matrices containing ints/floats
    You can assume all elements in the same dimension are of t same type/shape
    You must return a new matrix
    If you cannot concatenate the matrices, return None
    You can assume that mat1 and mat2 are never empty

"""


def cat_matrices(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """

    if axis == 0:
        return mat1 + mat2
    else:
        # if the list contains more lists
        if type(mat1[0]) is list:
            # for each sublist in the current list
            new_list = []
            for i in range(len(mat1)):
                # append of response of the recursive call of the function
                new_list.append(cat_matrices(mat1[i], mat2[i], axis-1))

            return new_list
        # if the list contains numbers
        else:

            return None


def matrix_shape(matrix):
    """ calculates the shape of a matrix: """
    if type(matrix) is list:
        response = [len(matrix)]
        response.extend(matrix_shape(matrix[0]))
        return response
    return []
