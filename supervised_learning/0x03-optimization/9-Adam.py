#!/usr/bin/env python3

""" Defines a function that updates a variable in place using
the Adam optimization algorithm
"""


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """ that updates a variable in place using the Adam optimization algorithm

    Parameters:
    -----------
    alpha : float
        is the learning rate
    beta1 : float
        is the weight used for the first moment
    beta2 : float
        is the weight used for the second moment
    epsilon : float
        is a small number to avoid division by zero
    var : numpy.ndarray
        containing the variable to be updated
    grad : numpy.ndarray
        containing the gradient of var
    v:
        the previous first moment of var
    s:
        the previous second moment of var
    t:
        the time step used for bias correction

    Returns:
    --------
    numpy.ndarray
        the updated variable
    numpy.ndarray
        the new first moment
    numpy.ndarray
        the new second moment
    """

    v = beta1 * v + (1 - beta1) * grad
    s = beta2 * s + (1 - beta2) * (grad ** 2)

    w = v / (1 - (beta1 ** t))
    b = s / (1 - (beta2 ** t))
    var -= alpha * w / ((b ** 0.5) + epsilon)
    return var, v, s
