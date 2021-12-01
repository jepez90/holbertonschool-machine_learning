#!/usr/bin/env python3
""" Function that concatenates two matrices along a specific axis """


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """

    if axis == 0:
        # copy the first array
        mat3 = mat1[:]

        # add the second array
        mat3.extend(mat2)

    else:
        mat3 = []

        # run trough first matrix and get each index and row
        for i, row2 in enumerate(mat2):

            # creates a copy of the row of the mat1
            new_row = mat1[i][:]

            # append the elements of the row from the mat2
            new_row.extend(row2)

            # add the new row to the new matrix
            mat3.append(new_row)

    return mat3
