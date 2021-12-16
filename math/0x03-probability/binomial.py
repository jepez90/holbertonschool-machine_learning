#!/usr/bin/env python3
""" defines class Binomial that represents a binomial distribution """


class Binomial:
    """ represents a binomial distribution """

    E = 2.7182818285
    PI = 3.1415926536

    def __init__(self, data=None, n=1, p=0.5):
        """
        data is a list of the data to be used to estimate the distribution
        n is the number of Bernoulli trials
        p is the probability of a “success”
        Sets the instance attributes n and p
            Saves n as an integer and p as a float
        If data is not given (i.e. None)
            Use the given n and p
            If n is not a positive value, raise a ValueError with the message
            n must be a positive value
            If p is not a valid probability, raise a ValueError with the
            message p must be greater than 0 and less than 1
        If data is given:
            Calculate n and p from data
            Round n to the nearest integer (rounded, not casting!
            The difference is important: int(3.7) is not the same as round(3.7)
            Hint: Calculate p first and then calculate n. Then recalculate p.
            Think about why you would want to do it this way?
            If data is not a list, raise a TypeError with the message 'data
            must be a list'
            If data does not contain at least two data points, raise a
            ValueError with the message 'data must contain multiple values'
        """
        self.n = int(n)
        self.p = float(p)
        if data is None:
            if self.n <= 0:
                raise ValueError("n must be a positive value")

            if self.p < 0 or self.p > 1:
                raise ValueError("p must be greater than 0 and less than 1")

        else:

            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # calc variance
            mean = float(sum(data)/len(data))
            sigmaSquared = sum([((i - mean)**2) for i in data])/(len(data))

            # cals p
            p = 1 - (sigmaSquared/mean)

            # cals n
            n = sigmaSquared/((1-self.p)*self.p)
            self.n = round(n)

            self.p = p

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of “successes”
        k is the number of “successes”
            If k is not an integer, convert it to an integer
            If k is out of range, return 0
        Returns the PMF value for k
        """
        if k < 0:
            return 0

        k = k if type(k) is int else int(k)

        n = self.n
        p = self.p
        q = 1-p
        nPx = self.fact(n)/(self.fact(k) * self.fact(n-k))

        return nPx * (p**k) * (q**(n-k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of “successes”
        k is the number of “successes”
            If k is not an integer, convert it to an integer
            If k is out of range, return 0
        Returns the CDF value for k
        Hint: use the pmf method
        """
        if k < 0:
            return 0

        k = k if type(k) is int else int(k)

        sum = 0
        for i in range(0, k+1):
            sum += self.pmf(i)

        return sum

    def fact(self, x):
        """ Calculates the factorial of a given number """
        if x == 0:
            return 1

        factX = x
        for i in range(2, x):
            factX *= i

        return factX
