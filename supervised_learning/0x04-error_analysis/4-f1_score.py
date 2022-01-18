#!/usr/bin/env python3
""" function that calculates the F1 score of a confusion matrix """

sensitivity = __import__('1-sensitivity').sensitivity
precision = __import__('2-precision').precision


def f1_score(confusion):
    """ calculates the F1 score of a confusion matrix

    Parameters:
    -----------
    confusion : numpy.ndarray
        is a confusion numpy.ndarray of shape (classes, classes) where row
        indices represent the correct labels and column indices represent the
        predicted labels where classes is the number of classes.

    Returns:
    --------
    numpy.ndarray
        of shape (classes,) containing the F1 score of each class
    """

    PPV = precision(confusion)
    TPR = sensitivity(confusion)
    return 2 * PPV * TPR / (PPV + TPR)
