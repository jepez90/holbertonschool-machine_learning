#!/usr/bin/env python3
""" defines the class Poisson that represents a poisson distribution: """


class Poisson:
    """ represents a poisson distribution: """

    E = 2.7182818285

    def __init__(self, data=None, lambtha=1.):
        """
        data is a list of the data to be used to estimate the distribution
        lambtha is the expected number of occurences in a given time frame
        Sets the instance attribute lambtha

        Saves lambtha as a float

        If data is not given, (i.e. None (be careful: not data has not the same
         result as data is None)):

            Use the given lambtha
            If lambtha is not a positive value or equals to 0, raise a
            ValueError with the message lambtha must be a positive value

        If data is given:

            Calculate the lambtha of data
            If data is not a list, raise a TypeError with the message data
             must be a list
            If data does not contain at least two data points, raise a
            ValueError with the message data must contain multiple values
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of “successes”
        k is the number of “successes”
            If k is not an integer, convert it to an integer
            If k is out of range, return 0
        Returns the PMF value for k

        """

        if type(k) != int:
            k = int(k)

        # k out of range
        if k < 0:
            return 0

        # calk k!
        kFactorial = 1
        for i in range(1, k + 1):
            kFactorial *= i

        lamb = self.lambtha
        # calc pfm = {lambda ^{k}*e^{-lambda }}/{k!}}
        return ((lamb**k)*(self.E**-lamb))/kFactorial

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of “successes”
        k is the number of “successes”
            If k is not an integer, convert it to an integer
            If k is out of range, return 0
        Returns the CDF value for k
        """

        if type(k) != int:
            k = int(k)

        # k out of range
        if k < 0:
            return 0

        lamb = self.lambtha
        iFactorial = 1
        sum = 1

        for i in range(1, k + 1):
            iFactorial *= i
            sum += (lamb**i)/iFactorial

        return (self.E**-lamb)*sum
