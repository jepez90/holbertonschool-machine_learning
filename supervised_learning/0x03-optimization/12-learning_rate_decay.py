#!/usr/bin/env python3
""" Defines a function that creates a learning rate decay operation
in tensorflow using inverse time decay
"""
import tensorflow.compat.v1 as tf


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """ creates a learning rate decay operation in tensorflow using
    inverse time decay in a stepwise fashion

    Parameters:
    -----------
    alpha : float
        the original learning rate
    decay_rate : float
        the weight used to determine the rate at which alpha will decay
    global_step : int
        the number of passes of gradient descent that have elapsed
    decay_step : int
        the number of passes of gradient descent that should occur before
        alpha is decayed further

    Returns:
    --------
    float
        the learning rate decay operation
    """

    return tf.train.inverse_time_decay(
        alpha, global_step, decay_step, decay_rate, staircase=True)
