#!/usr/bin/env python3
""" define a function that returns two placeholders, x and y,
for the neural network
"""
import tensorflow.compat.v1 as tf


def create_layer(prev, n, activation):
    """  creates a layer

    Args:

      prev: is the tensor output of the previous layer
      n: is the number of nodes in the layer to create
      activation: is the activation function that the layer should use.
    """

    initializer = tf.keras.initializers.VarianceScaling(mode='fan_avg')
    new_layer = tf.keras.layers.Dense(
        units=n,
        activation=activation,
        kernel_initializer=initializer,
        name="layer"
    )
    return new_layer
