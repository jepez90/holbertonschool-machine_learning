#!/usr/bin/env python3
"""  Function that adds two arrays element-wise """


def add_arrays(arr1, arr2):
    """ adds two arrays element-wise """

    if len(arr1) == len(arr2):
        return [arr1[i] + arr2[i] for i in range(len(arr1))]

    return None
