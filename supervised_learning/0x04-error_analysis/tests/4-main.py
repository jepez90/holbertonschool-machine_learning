#!/usr/bin/env python3

import sys
import os
import numpy as np
sys.path.append(os.path.abspath('..'))
f1_score = __import__('4-f1_score').f1_score

if __name__ == '__main__':
    confusion = np.load('confusion.npz')['confusion']

    np.set_printoptions(suppress=True)
    print(f1_score(confusion))
