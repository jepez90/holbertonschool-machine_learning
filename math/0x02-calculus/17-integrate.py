#!/usr/bin/env python3
"""
Write a function def poly_integral(poly, C=0): that calculates the integral
of a polynomial:

    poly is a list of coefficients representing a polynomial
    the index of the list represents the power of x that the coeff belongs to
        Example: if [f(x) = x^3 + 3x +5] , poly is equal to [5, 3, 0, 1]
    C is an integer representing the integration constant
    If a coefficient is a whole number, it should be represented as an integer
    If poly or C are not valid, return None
    Return a new list of coeff representing the integral of the polynomial
    The returned list should be as small as possible

"""


def poly_integral(poly, C=0):
    """ calculates the integral of a polynomial """
    # store the result
    integ = [C]

    # the list must have at least one element
    if type(poly) is not list or len(poly) == 0:
        return None

    # run throug all element in the list and multiply it for it's index
    # to get the derivate, the index i is the power.
    for i, coeff in enumerate(poly):
        # check if each element is a number
        if type(coeff) not in [int, float]:
            return None

        # add the multiplication to the result list
        integ.append((coeff)/(i+1))

    return [int(i) if int(i)==i else i for i in integ]
