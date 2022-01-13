#!/usr/bin/env python3
""" defines a function hat normalizes (standardizes) a matrix """


def normalize(X, m, s):
    """ function that normalizes (standardizes) a matrix

    Args:
        X: `numpy.ndarray` of shape `(d, nx)` to normalize, where
            `d` is the number of data points and
            `nx` is the number of features
        m: `numpy.ndarray` of shape `(nx,)` that contains the mean of all
            features of `X`
        s: `numpy.ndarray` of shape `(nx,)` that contains the standard
        deviation of all features of `X`

    Returns: The normalized `X` matrix
    """

    return (X - m) / s
