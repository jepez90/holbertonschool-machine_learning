#!/usr/bin/env python3
""" function that calculates the precision for each class in a confusion matrix
"""
import numpy as np


def precision(confusion):
    """ calculates the precision for each class in a confusion matrix

    Parameters:
    -----------
    confusion : numpy.ndarray
        is a confusion numpy.ndarray of shape (classes, classes) where row
        indices represent the correct labels and column indices represent the
        predicted labels where classes is the number of classes.

    Returns:
    --------
    numpy.ndarray
        of shape (classes,) containing the precision of each class
"""
    TP = confusion.diagonal()
    FP = np.sum(confusion, axis=0)
    return TP / FP
