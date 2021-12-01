#!/usr/bin/env python3
""" 
    Function that performs matrix multiplication
    
    You can assume that mat1 and mat2 are 2D matrices containing ints/floats
    You can assume all elements in the same dimension are of the same type/shape
    You must return a new matrix
    If the two matrices cannot be multiplied, return None

"""


def mat_mul(mat1, mat2):
    """ performs matrix multiplication """

    shape1 = [len(mat1), len(mat1[0])]
    shape2 = [len(mat2), len(mat2[0])]

    if shape1[1] != shape2[0]:
        return None

    new_matrix = []

    # to run through the rows of the mat1
    for i in range(shape1[0]):
        new_row = []

        # to run through the each column in each row of the mat2
        for j in range(shape2[1]):
            n = 0

            # to run through the each column in each row of the mat1
            for k in range(shape1[1]):
                n += (mat1[i][k] * mat2[k][j])

            new_row.append(n)

        new_matrix.append(new_row)

    return new_matrix
