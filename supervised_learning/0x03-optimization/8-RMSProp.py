""" Defines a function that creates the training operation for a
neural network in tensorflow using the RMSProp optimization algorithm
"""
import tensorflow.compat.v1 as tf


def create_RMSProp_op(loss, alpha, beta2, epsilon):
    """ creates the training operation for a neural network in tensorflow
    using the RMSProp optimization algorithm

    Parameters:
    -------
    loss : tensor
        the loss of the network
    alpha : float
        the learning rate
    beta2 : int
        the RMSProp weight
    epsilon : float
        is a small number to avoid division by zero

    Returns:
    --------
    Tensor
        the RMSProp optimization operation
    """
    RMSProp_optimizer = tf.train.RMSPropOptimizer(
        alpha, beta2, epsilon=epsilon)
    return RMSProp_optimizer.minimize(loss)
