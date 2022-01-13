#!/usr/bin/env python3
"""function that updates the learning rate using inverse time decay in numpy"""


def learning_rate_decay(alpha, decay_rate, global_step, decay_step):
    """ updates the learning rate using inverse time decay in numpy
    in a stepwise fashion

    Parameters:
    -----------
    alpha : float
        the original learning rate
    decay_rate: float
        the weight used to determine the rate at which alpha will decay
    global_step : int
        the number of passes of gradient descent that have elapsed
    decay_step : int
        the number of passes of gradient descent that should occur before
        alpha is decayed further

    Returns:
    --------
    float
        the updated value for alpha
    """
    epoch = int(global_step / decay_step)
    return alpha / (1 + (decay_rate * epoch))
