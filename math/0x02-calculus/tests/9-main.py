#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath('..'))

summation_i_squared = __import__('9-sum_total').summation_i_squared

n = 5
print(summation_i_squared(n))
