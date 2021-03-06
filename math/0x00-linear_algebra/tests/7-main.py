#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.abspath('..'))

cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D

mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [55, 66]]
mat3 = [[7], [8]]
mat4 = cat_matrices2D(mat1, mat2)
mat5 = cat_matrices2D(mat1, mat3, axis=1)
print(mat4)
print(mat5)
mat2[0] = [9, 10]
mat2[1].append(5)
print(mat1)
print(mat4)
print(mat5)
