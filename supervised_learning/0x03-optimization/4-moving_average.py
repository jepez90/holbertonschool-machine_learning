#!/usr/bin/env python3
""" Defines a function that calculates the weighted moving average
of a data set
"""


def moving_average(data, beta):
    """ calculates the weighted moving average of a data set

    Parameters
    ----------
    data : list
        data to calculate the moving average of
    beta : float
        weight used for the moving average

    Returns
    -------
    list
        containing the moving averages of data
    """
    Vt = 0
    avg_data = []
    for t in range(0, len(data)):
        Vt = beta * Vt + (1-beta) * data[t]
        avg_data.append(Vt/(1-beta**(t + 1)))
    return avg_data
