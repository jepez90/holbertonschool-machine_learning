#!/usr/bin/env python3
"""
    Function that slices a matrix along specific axes:

    You can assume that matrix is a numpy.ndarray
    You must return a new numpy.ndarray
    axes is a dictionary where the key is an axis to slice along and the value
    is a tuple representing the slice to make along that axis
    You can assume that axes represents a valid slice
"""


def np_slice(matrix, axes={}):
    """ slices a matrix along specific axes """

    # get the dimensions, number of axis of the array
    dimensions = max(axes.keys()) + 1

    # creates an list with len  = dimensions an initialized in None
    slicer = [Ellipsis]*dimensions

    # traverse the dict of aces
    for key, value in axes.items():

        # add each slicer in the list at the corresponding axe
        slicer[key] = slice(*value)

    # apply the slicer and creates a copy o the sliced array
    return matrix[tuple(slicer)].copy()
