#!/usr/bin/env python3
""" defines the Normal that represents a normal distribution """


class Normal:
    """ represents a normal distribution """

    E = 2.7182818285
    PI = 3.1415926536

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        data is a list of the data to be used to estimate the distribution
        mean is the mean of the distribution
        stddev is the standard deviation of the distribution
        Sets the instance attributes mean and stddev
            Saves mean and stddev as floats
        If data is not given (i.e. None (be careful: not data has not the same
        result as data is None))
            Use the given mean and stddev
            If stddev is not a positive value or equals to 0, raise a
            ValueError with the message 'stddev must be a positive value'
        If data is given:
            Calculate the mean and standard deviation of data
            If data is not a list, raise a TypeError with the message
            'data must be a list'
            If data does not contain at least two data points, raise a
            ValueError with the message 'data must contain multiple values'
        """
        self.mean = float(mean)
        self.stddev = float(stddev)
        if data is None:
            if self.stddev <= 0:
                raise ValueError("stddev must be a positive value")
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # calc mean
            self.mean = float(sum(data)/len(data))

            # cals sd
            s = [abs(x - (self.mean))**2 for x in data]
            self.stddev = (sum(s) / len(data))**(1/2)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
        x is the x-value
        Returns the z-score of x
        """
        return (x-self.mean)/self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score
        z is the z-score
        Returns the x-value of z
        """
        return (self.mean + self.stddev * z)

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value
        x is the x-value
        Returns the PDF value for x
        """
        sigma = self.stddev
        num = sigma*((2*self.PI)**(1/2))
        exp = -((x-self.mean)**2)/(2*(sigma**2))
        return (self.E**exp)/num

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value
        x is the x-value
        Returns the CDF value for x
        """
        erf = self.erf((x-self.mean)/(self.stddev*((2)**(1/2))))
        return (1 + erf)/2

    def erf(self, x):
        idxs = range(1, 6)

        exp = [2*i - 1 for i in idxs]
        denom = [1-(2*i) if i % 2 == 0 else (2*i) - 1 for i in idxs]

        f = []
        for i in range(0, 5):
            f.append((x**exp[i])/denom[i])

        return 2*(sum(f))/((self.PI)**(1/2))
