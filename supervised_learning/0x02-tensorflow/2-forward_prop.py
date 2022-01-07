#!/usr/bin/env python3
"""function that creates the forward propagation graph for neural network"""

import tensorflow.compat.v1 as tf
create_layer = __import__('1-create_layer').create_layer


def forward_prop(x, layer_sizes=[], activations=[]):
    """creates the forward propagation graph for the neural network

    Args:
        x: is the placeholder for the input data
        layer_sizes: is a list containing the number of nodes in each layer
            of the network.
        activations: is a list containing the activation functions for each
            layer of the network

    Returns:
        Tensor: the prediction of the network in tensor form
    """

    input = x
    for i, size in enumerate(layer_sizes):
        input = create_layer(input, size, activations[i])

    return input
