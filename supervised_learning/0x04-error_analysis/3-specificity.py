#!/usr/bin/env python3
""" function that calculates the specificity for each class in a
confusion matrix
"""
import numpy as np


def specificity(confusion):
    """ that calculates the specificity for each class in a confusion matrix

    Parameters:
    -----------
    confusion : numpy.ndarray
        is a confusion numpy.ndarray of shape (classes, classes) where row
        indices represent the correct labels and column indices represent the
        predicted labels where classes is the number of classes.

    Returns:
    --------
    numpy.ndarray
        of shape (classes,) containing the specificity of each class
"""
    T = np.array([np.sum(confusion)] * confusion.shape[0])

    FN = np.sum(confusion, axis=0)
    FP = np.sum(confusion, axis=1)
    TP = confusion.diagonal()

    TN = T - FN - FP + TP
    FP = FN - TP

    return TN/(TN + FP)
