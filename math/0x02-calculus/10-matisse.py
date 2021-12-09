#!/usr/bin/env python3

"""
function def poly_derivative(poly): that calculates the derivative
of a polynomial:

    poly is a list of coefficients representing a polynomial
    the index of the list represents the power of x that the coeff belongs to
        Example: if [f(x) = x^3 + 3x +5] , poly is equal to [5, 3, 0, 1]
    If poly is not valid, return None
    If the derivative is 0, return [0]
    Return a new list of coeff representing the derivative of the polynomial

"""


def poly_derivative(poly):
    # store the result
    deriv = []

    # variable to check if the derivate is 0
    add = 0

    # the list must have at least one element
    if len(poly) == 0:
        return None

    # run throug all element in the list and multiply it for it's index
    # to get the derivate, the index i is the power.
    for i, coeff in enumerate(poly):
        # check if each element is a number
        if type(coeff) not in [int, float]:
            return None

        # add the multiplication to the result list
        deriv.append(i*coeff)

        # adds the absolute value of the new coheff
        add += abs(i*coeff)

    # if add is 0, the derivate is 0
    if add == 0:
        return [0]
    else:
        # slice the list removing the first element
        return deriv[1:]
