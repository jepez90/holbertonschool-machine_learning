#!/usr/bin/env python3
"""
    Function that adds two matrices:

    You can assume that mat1 and mat2 are matrices containing ints/floats
    You can assume all elements in the same dimension are of t same type/shape
    You must return a new matrix
    If matrices are not the same shape, return None
    You can assume that mat1 and mat2 will never be empty
"""
import numpy as np


def add_matrices(mat1, mat2):
    """ adds two matrices """

    # convert list in nparray
    np_mat1 = np.array(mat1)
    np_mat2 = np.array(mat2)

    if np_mat1.shape != np_mat2.shape:
        return None

    # adds the arrays
    mat_sum = np_mat1 + np_mat2

    # convert the nparray in list
    return mat_sum.tolist()
