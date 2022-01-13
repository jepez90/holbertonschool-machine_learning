#!/usr/bin/env python3
""" defines a function that calculates the normalization (standardization)
constants of a matrix.
"""
import numpy as np


def normalization_constants(X):
    """calculates the normalization (standardization) constants of a matrix.

    Args:
        X: `numpy.ndarray` of shape (m, nx) to normalize where
            `m` is the number of data points and
            `nx` is the number of features.

    Returns: the mean and standard deviation of each feature, respectively
    """

    sigma = X.std(axis=0)
    mean = X.mean(axis=0)

    return mean, sigma


if __name__ == '__main__':
    """ test """
    np.random.seed(0)
    a = np.random.normal(0, 2, size=(100, 1))
    b = np.random.normal(2, 1, size=(100, 1))
    c = np.random.normal(-3, 10, size=(100, 1))
    X = np.concatenate((a, b, c), axis=1)
    m, s = normalization_constants(X)
    print(m)
    print(s)
