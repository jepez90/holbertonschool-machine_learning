#!/usr/bin/env python3
""" Defines a function that updates a variable using the
RMSProp optimization algorithm
"""


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """ updates a variable using the RMSProp optimization algorithm

    Parameters:
    ----------
        alpha : float
            is the learning rate
        beta2 : float
            is the RMSProp weight
        epsilon : float
            is a small number to avoid division by zero
        var : numpy.ndarray
            containing the variable to be updated
        grad : numpy.ndarray
            containing the gradient of var
        s :
            is the previous second moment of var

    Returns:
    --------
    numpy.ndarray
        the updated variable var
    numpy.ndarray
        the new moment
    """
    sdw = (beta2 * s) + (1-beta2) * (grad ** 2)

    var -= (alpha * grad / (sdw ** (0.5) + epsilon))

    return var, sdw
