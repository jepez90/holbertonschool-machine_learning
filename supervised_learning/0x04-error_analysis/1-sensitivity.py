#!/usr/bin/env python3
""" Function that calculates the sensitivity for each class in a confusion
matrix
"""
import numpy as np


def sensitivity(confusion):
    """  calculates the sensitivity for each class in a confusion matrix:

    Parameters:
    confusion : numpy.ndarray
        is a confusion numpy.ndarray of shape (classes, classes) where row
        indices represent the correct labels and column indices represent the
        predicted labels where classes is the number of classes.

    Returns:
    --------
    numpy.ndarray
        of shape (classes,) containing the sensitivity of each class
    """
    TP = confusion.diagonal()
    P = np.sum(confusion, axis=1).T
    return TP / P
