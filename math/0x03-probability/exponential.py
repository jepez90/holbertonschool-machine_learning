#!/usr/bin/env python3
""" defines the Exponential that represents an exponential distribution """


class Exponential:
    """ represents an exponential distribution """

    E = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data to be used to estimate the distribution
        lambtha is the expected number of occurences in a given time frame
        Sets the instance attribute lambtha
            Saves lambtha as a float
        If data is not given (i.e. None):
            Use the given lambtha
            If lambtha is not a positive value, raise a ValueError with the
            message 'lambtha must be a positive value'
        If data is given:
            Calculate the lambtha of data
            If data is not a list, raise a TypeError with the message 'data
            must be a list'
            If data does not contain at least two data points, raise a
            ValueError with the message 'data must contain multiple values'
        """
        self.lambtha = float(lambtha)
        if data is None:
            if self.lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # calc lambtha
            self.lambtha = float(len(data)/sum(data))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
        x is the time period
        Returns the PDF value for x
        If x is out of range, return 0
        """
        # x out of range
        if x < 0:
            return 0

        lamb = self.lambtha

        # calc pdf = {lambda * e^{-lambda * x }}
        return (lamb * (self.E**(-lamb * x)))

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given time period
        x is the time period
        Returns the CDF value for x
        If x is out of range, return 0
        """

        # x out of range
        if x < 0:
            return 0

        lamb = self.lambtha

        # calc cdf = {1 - e^{-lambda * x }}
        return (1 - (self.E**(-lamb * x)))
