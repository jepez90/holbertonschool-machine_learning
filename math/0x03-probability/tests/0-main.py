#!/usr/bin/env python3

import numpy as np
import sys
import os
sys.path.append(os.path.abspath('..'))
Poisson = __import__('poisson').Poisson

np.random.seed(0)
p1 = Poisson([2, 8, 0, 0, 8, 9, 10, 7, 10, 0, 10, 6, 3, 2, 6, 10, 8, 9, 0, 8,
              10, 1, 6, 1, 5, 4, 5, 5, 1, 4, 2, 0, 2, 4, 1, 0, 1, 3, 4, 0, 1,
              4, 6, 6, 5, 8, 0, 0, 7, 8, 4, 3, 10, 8, 8, 2, 9, 3, 10, 6, 4, 2,
              5, 4, 4, 3, 9, 8, 2, 2, 7, 5, 7, 1, 2, 5, 5, 2, 5, 10, 3, 9, 9,
              9, 3, 2, 4, 4, 9, 3, 8, 9, 9, 8, 7, 0, 6, 7, 8, 10]
             )

print('Lambtha:', p1.lambtha)


data = np.random.poisson(5., 100)
p1 = Poisson(data.tolist())
print('Lambtha:', p1.lambtha)


p2 = Poisson(lambtha=5)
print('Lambtha:', p2.lambtha)
