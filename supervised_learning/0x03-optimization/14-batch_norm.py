#!/usr/bin/env python3
""" defines a function that creates a batch normalization layer for
a neural network in tensorflow
"""
import tensorflow.compat.v1 as tf


def create_batch_norm_layer(prev, n, activation):
    """ creates a batch normalization layer for a neural network in tensorflow:

    Parameters:
    -----------
    prev :
        the activated output of the previous layer
    n :
        the number of nodes in the layer to be created
    activation :
        the activation function that should be used on the output of the layer

    Returns:
    --------
    tensor
        of the activated output for the layer
    """
    kernel = tf.variance_scaling_initializer(mode="fan_avg")
    layer = tf.layers.Dense(units=n, name="layer",
                            kernel_initializer=kernel)

    p = layer(prev)
    mean, variance = tf.nn.moments(p, [0])

    gamma = tf.ones([n])
    beta = tf.zeros([n])

    norm = tf.nn.batch_normalization(p, mean, variance, beta, gamma, 1e-8)

    return activation(norm)
