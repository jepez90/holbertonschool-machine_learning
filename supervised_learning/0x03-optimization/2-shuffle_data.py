#!/usr/bin/env python3
"""  Defines a function that shuffles the data points in two matrices
the same way
"""
import numpy as np


def shuffle_data(X, Y):
    """ Function that shuffles the data points in two matrices the same way:

    Args:
    -----
        X: first `numpy.ndarray` of shape `(m, nx)` to shuffle, where
            `m` is the number of data points and
            `nx` is the number of features in `X`.
        Y: second `numpy.ndarray` of shape `(m, ny)` to shuffle,where
            `m` is the same number of data points as in `X` and
            `ny` is the number of features in `Y`

    Returns: the shuffled `X` and `Y` matrices
    """
    new_idxs = np.random.permutation(X.shape[0])
    X = X[new_idxs]
    Y = Y[new_idxs]
    return X, Y


if __name__ == '__main__':
    """ Test """
    X = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])
    Y = np.array([[11, 12],
                  [13, 14],
                  [15, 16],
                  [17, 18],
                  [19, 20]])

    np.random.seed(0)
    X_shuffled, Y_shuffled = shuffle_data(X, Y)

    print(X_shuffled)
    print(Y_shuffled)
