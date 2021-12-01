#!/usr/bin/env python3
"""  Function that adds two matrices element-wise """


def add_matrices2D(mat1, mat2):
    """ adds two matrices element-wise """

    shape1 = [len(mat1), len(mat1[0])]
    shape2 = [len(mat2), len(mat2[0])]

    if shape1 != shape2:
        return None

    response = []

    # run trough first matrix and get each index and row
    for i, row1 in enumerate(mat1):
        row2 = mat2[i]
        # add each element of the both list or rows and generates a new row
        new_row = [row1[j] + row2[j] for j in range(shape1[1])]
        response.append(new_row)

    return response
