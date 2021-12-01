#!/usr/bin/env python3
""" Function that calculates the shape of a matrix: """


def matrix_shape(matrix):
    """ calculates the shape of a matrix: """
    if type(matrix) is list:
        response = [len(matrix)]
        response.extend(matrix_shape(matrix[0]))
        return response
    return []
