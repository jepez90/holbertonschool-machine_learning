#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath('..'))

poly_derivative = __import__('10-matisse').poly_derivative

poly = [0, 6, -3, 0]
print(poly_derivative(poly))
