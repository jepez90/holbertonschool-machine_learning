#!/usr/bin/env python3
""" function that normalizes an unactivated output of a neural network
using batch normalization
"""
import numpy as np


def batch_norm(Z, gamma, beta, epsilon):
    """ normalizes an unactivated output of a neural network using
    batch normalization

    Parameters:
    -----------
    Z : numpy.ndarray
        of shape (m, n) that should be normalized
        m is the number of data points
        n is the number of features in Z
    gamma : numpy.ndarray
        of shape (1, n) containing the scales used for batch normalization
    beta : numpy.ndarray
        of shape (1, n) containing the offsets used for batch normalization
    epsilon : float
        small number used to avoid division by zero

    Returns:
    --------
    numpy.ndarray
        the normalized Z matrix
    """

    mean = np.mean(Z, axis=0)
    var = np.var((Z - mean), axis=0)

    normalized = (Z - mean) / (np.sqrt(var + epsilon))
    return gamma * normalized + beta
