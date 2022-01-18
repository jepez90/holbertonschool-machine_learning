#!/usr/bin/env python3

import sys
import os
import numpy as np
sys.path.append(os.path.abspath('..'))
sensitivity = __import__('1-sensitivity').sensitivity

if __name__ == '__main__':
    confusion = np.load('confusion.npz')['confusion']

    np.set_printoptions(suppress=True)
    print(sensitivity(confusion))
