#!/usr/bin/env python3
""" Defines a function that updates a variable using the gradient descent
with momentum optimization algorithm
"""


def update_variables_momentum(alpha, beta1, var, grad, v):
    """ updates a variable using the gradient descent with momentum
    optimization algorithm

    Parameters:
    -------
    alpha:
        the learning rate
    beta1:
        the momentum weight
    var: numpy.ndarray
        containing the variable to be updated
    grad: numpy.ndarray
        containing the gradient of var
    v: numpy.ndarray
        is the previous first moment of var

    Returns:
    -------
    numpy.ndarray
        the updated variable var
    numpy.ndarray
        the new moment
    """

    new_momentum = (beta1 * v) + (1-beta1)*grad

    var -= (alpha * new_momentum)

    return var, new_momentum
