#!/usr/bin/env python3

import sys
import os
import numpy as np
sys.path.append(os.path.abspath('..'))
specificity = __import__('3-specificity').specificity

if __name__ == '__main__':
    confusion = np.load('confusion.npz')['confusion']

    np.set_printoptions(suppress=True)
    print(specificity(confusion))
