#!/usr/bin/env python3
""" Function that concatenates two matrices along a specific axis """


def cat_matrices2D(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis """

    _mat1 = [row[:] for row in mat1]
    _mat2 = [row[:] for row in mat2]

    if axis == 0:
        return _mat1 + _mat2
    else:
        return [_mat1[i] + _mat2[i] for i in range(len(_mat1))]
