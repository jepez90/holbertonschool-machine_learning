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

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    def forward_prop(self, X):
        """
        Calculates the forward propagation of the neuron
        X is a numpy.ndarray with shape (nx, m) that contains the input data
            nx is the number of input features to the neuron
            m is the number of examples
            The neuron should use a sigmoid activation function
            Updates and Returns the private attribute __A
        """
        z = np.matmul(self.__W, X) + self.__b
        self.__A = 1/(1+np.exp(-z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression
            Y is a numpy.ndarray with shape (1, m) that contains the correct
                labels for the input data
            A is a numpy.ndarray with shape (1, m) containing the activated
                output of the neuron for each example
        To avoid division by zero errors, use 1.0000001 - A instead of 1 - A
        Returns the cost
        """
        L = (Y*np.log(A)+(1-Y)*np.log(1.0000001-A))
        return -L.sum()/Y.shape[1]

    @property
    def W(self):
        """ get the weights vector for the neuron """
        return self.__W

    @property
    def b(self):
        """ get the bias for the neuron"""
        return self.__b

    @property
    def A(self):
        """ get the activated output of the neuron (prediction). """
        return self.__A
