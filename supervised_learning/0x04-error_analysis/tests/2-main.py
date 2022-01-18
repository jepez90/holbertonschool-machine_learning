#!/usr/bin/env python3

import sys
import os
import numpy as np
sys.path.append(os.path.abspath('..'))
precision = __import__('2-precision').precision

if __name__ == '__main__':
    confusion = np.load('confusion.npz')['confusion']

    np.set_printoptions(suppress=True)
    print(precision(confusion))
