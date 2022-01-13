#!/usr/bin/env python3
""" Defines a function that creates the training operation for a neural
network in tensorflow using the gradient descent with
momentum optimization algorithm
"""
import tensorflow.compat.v1 as tf


def create_momentum_op(loss, alpha, beta1):
    """ creates the training operation for a neural network in tensorflow
    using the gradient descent with momentum optimization algorithm

    Parameters:
    -------
    loss : tensor
        the loss of the network
    alpha : float
        the learning rate
    beta1 : int
        the momentum weight

    Returns
    -------
    tensor
        the momentum optimization operation
    """

    momentum_optmizer = tf.train.MomentumOptimizer(alpha, beta1)
    return momentum_optmizer.minimize(loss)
