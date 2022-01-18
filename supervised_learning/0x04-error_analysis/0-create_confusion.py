#!/usr/bin/env python3

""" Function that creates a confusion matrix """
import numpy as np


def create_confusion_matrix(labels, logits):
    """ creates a confusion matrix:

    Parameters:
    -----------
    labels : numpy.ndarray
        is a one-hot numpy.ndarray of shape `(m, classes)` containing the
        correct labels for each data point. where `m` is the number of data
        points and `classes` is the number of classes.
    logits : numpy.ndarray
        is a one-hot numpy.ndarray of shape `(m, classes)` containing the
        predicted labels

    Returns:
    --------
    a confusion numpy.ndarray of shape (classes, classes) with row indices
    representing the correct labels and column indices representing the
    predicted labels
    """
    return np.matmul(labels.transpose(), logits)
