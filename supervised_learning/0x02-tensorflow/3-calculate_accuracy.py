#!/usr/bin/env python3
""" defines a function that calculates the accuracy of a prediction """

import tensorflow.compat.v1 as tf


def calculate_accuracy(y, y_pred):
    """ calculates the accuracy of a prediction

    Args:
        y: placeholder for the labels of the input data
        y_pred: tensor containing the network’s predictions

    Returns:
        Tensor containing the decimal accuracy of the prediction
    """

    correct_predictions = tf.cast(tf.equal(y, y_pred), tf.float32)
    return tf.reduce_mean(correct_predictions)
