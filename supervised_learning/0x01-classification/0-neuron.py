#!/usr/bin/env python3
"""
Contine the class Neuron that defines a single neuron performing
binary classification
"""
import numpy as np


class Neuron:
    """ defines a single neuron performing binary classification
    Public instance attributes:
        W: The weights vector for the neuron. Upon instantiation,
            it should be initialized using a random normal distribution.
        b: The bias for the neuron. Upon instantiation,
            it should be initialized to 0.
        A: The activated output of the neuron (prediction).
            Upon instantiation, it should be initialized to 0.
    """

    def __init__(self, nx):
        """
        nx is the number of input features to the neuron
        If nx is not an integer, raise a TypeError with the exception:
            'nx must be an integer'
        If nx is less than 1, raise a ValueError with the exception:
            'nx must be a positive integer'
        """
        if type(nx) is not int:
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")
            
        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
