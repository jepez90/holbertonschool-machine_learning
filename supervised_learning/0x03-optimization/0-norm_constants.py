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
