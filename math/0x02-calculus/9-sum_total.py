#!/usr/bin/env python3

"""
Write a function def summation_i_squared(n): that calculates sum_{i=1}^{n} i^2:
    n is the stopping condition
    Return the integer value of the sum
    If n is not a valid number, return None
    You are not allowed to use any loops

"""


def summation_i_squared(n):
    """ that calculates sum_{i=1}^{n} i^2 : """
    if type(n) != int or n < 1:
        return None
    if n > 1:
        return summation_i_squared(n - 1) + n**2
    else:
        return 1
