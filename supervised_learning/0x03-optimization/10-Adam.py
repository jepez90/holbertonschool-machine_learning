#!/usr/bin/env python3
""" Defines a function that creates the training operation for a neural network
in tensorflow using the Adam optimization algorithm
"""
import tensorflow.compat.v1 as tf


def create_Adam_op(loss, alpha, beta1, beta2, epsilon):
    """ creates the training operation for a neural network in tensorflow
    using the Adam optimization algorithm

    Parameters:
    -----------
    loss : tensor
        the loss of the network
    alpha : float
        the learning rate
    beta1 : float
        the weight used for the first moment
    beta2 : float
        the weight used for the second moment
    epsilon : float
        a small number to avoid division by zero

    Returns:
    --------
    tensor
        the Adam optimization operation
    """

    adam_optimizer = tf.train.AdamOptimizer(
        alpha, beta1, beta2, epsilon=epsilon)
    return adam_optimizer.minimize(loss)
