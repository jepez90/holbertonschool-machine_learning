<div align=center>

***holbertonschool-machine_learning***
<hr />
 <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Logo Python" style="max-width:80%;">
 <hr />
<a href="https://twitter.com/Jepez90"><img src="https://img.shields.io/twitter/url?label=%40Jepez90&style=social&url=https%3A%2F%2Ftwitter.com%2FJepez90" alt="Logo Twitter">&nbsp;</a>
<a href="https://www.linkedin.com/in/jepez90/"><img src="https://img.shields.io/badge/jepez90-%230077B5.svg?&logo=linkedin&logoColor=white" alt="Logo LinkedIn">&nbsp;</a>
<img src="https://img.shields.io/badge/jepez90-white?style=flat&logo=gmail" alt="Logo Gmail">&nbsp;
<a href="https://twitter.com/HolbertonCOL"><img src="https://img.shields.io/badge/Holberton_School-red" alt="Logo Holberton">&nbsp;</a>

<a href="https://github.com/jepez90"><img src="https://visitor-badge.glitch.me/badge?page_id=jepez90.MachineLearning.0x00&" alt="badget visitors"></a>
</div>

# Project: 0x00. Linear Algebra

> Excercises about:
    <ul>
        <li>What is a vector?</li>
        <li>What is a matrix?</li>
        <li>What is a transpose?</li>
        <li>What is the shape of a matrix?</li>
        <li>What is an axis?</li>
        <li>What is a slice?</li>
        <li>How do you slice a vector/matrix?</li>
        <li>What are element-wise operations?</li>
        <li>How do you concatenate vectors/matrices?</li>
        <li>What is the dot product?</li>
        <li>What is matrix multiplication?</li>
        <li>What is Numpy?</li>
        <li>What is parallelization and why is it important?</li>
        <li>What is broadcasting?</li>
    </ul>


## Files in this Folder:

* <a href='0-slice_me_up.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **0-slice_me_up.py**</a><br />

Complete the following source code (found below):
```python
#!/usr/bin/env python3
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]
arr1 =  # your code here
arr2 =  # your code here
arr3 =  # your code here
print("The first two numbers of the array are: {}".format(arr1))
print("The last five numbers of the array are: {}".format(arr2))
print("The 2nd through 6th numbers of the array are: {}".format(arr3))
```

* <a href='1-trim_me_down.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **1-trim_me_down.py**</a><br />

Complete the following source code (found below):
```python
#!/usr/bin/env python3
matrix = [[1, 3, 9, 4, 5, 8], [2, 4, 7, 3, 4, 0], [0, 3, 4, 6, 1, 5]]
the_middle = []
# your code here
print("The middle columns of the matrix are: {}".format(the_middle))
```

* <a href='2-size_me_please.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **2-size_me_please.py**</a><br />

Function ***def matrix_shape(matrix):*** that calculates the shape of a matrix:

    You can assume all elements in the same dimension are of the same type/shape
    The shape should be returned as a list of integers


* <a href='3-flip_me_over.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **3-flip_me_over.py**</a><br />

Function ***def matrix_transpose(matrix):*** that returns the transpose of a 2D matrix, ***matrix***:

    You must return a new matrix
    You can assume that matrix is never empty
    You can assume all elements in the same dimension are of the same type/shape


* <a href='4-line_up.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **4-line_up.py**</a><br />

Function ***def add_arrays(arr1, arr2):*** that adds two arrays element-wise:

    You can assume that arr1 and arr2 are lists of ints/floats
    You must return a new list
    If arr1 and arr2 are not the same shape, return None


* <a href='5-across_the_planes.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **5-across_the_planes.py**</a><br />

Function ***def add_matrices2D(mat1, mat2):*** that adds two matrices element-wise:

* <a href='6-howdy_partner.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **6-howdy_partner.py**</a><br />

Function ***def cat_arrays(arr1, arr2):*** that concatenates two arrays:

* <a href='7-gettin_cozy.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **7-gettin_cozy.py**</a><br />

Function ***def cat_matrices2D(mat1, mat2, axis=0):*** that concatenates two matrices along a specific axis:

* <a href='8-ridin_bareback.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **8-ridin_bareback.py**</a><br />

Function ***def mat_mul(mat1, mat2):*** that performs matrix multiplication:

* <a href='9-let_the_butcher_slice_it.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **9-let_the_butcher_slice_it.py**</a><br />

Complete the following source code (found below):

* <a href='10-ill_use_my_scale.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **10-ill_use_my_scale.py**</a><br />

Function ***def np_shape(matrix):*** that calculates the shape of a ***numpy.ndarray***:

* <a href='11-the_western_exchange.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **11-the_western_exchange.py**</a><br />

Function ***def np_transpose(matrix):*** that transposes ***matrix***:

* <a href=' 12-bracin_the_elements.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> ** 12-bracin_the_elements.py**</a><br />

Function ***def np_elementwise(mat1, mat2):*** that performs element-wise addition, subtraction, multiplication, and division:

* <a href='13-cats_got_your_tongue.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **13-cats_got_your_tongue.py**</a><br />

Function ***def np_cat(mat1, mat2, axis=0)*** that concatenates two matrices along a specific axis:

* <a href='14-saddle_up.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **14-saddle_up.py**</a><br />

Function ***def np_matmul(mat1, mat2):*** that performs matrix multiplication:

* <a href='100-slice_like_a_ninja.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **100-slice_like_a_ninja.py**</a><br />

Function ***def np_slice(matrix, axes={}):*** that slices a matrix along specific axes:

* <a href='101-the_whole_barn.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **101-the_whole_barn.py**</a><br />

Function ***def add_matrices(mat1, mat2):*** that adds two matrices:

* <a href='102-squashed_like_sardines.py'><img src="https://raw.githubusercontent.com/jepez90/jepez90.github.io/master/img/Readme_media/logoPythonBasic.svg" alt="Logo Python" height="20" /> **102-squashed_like_sardines.py**</a><br />

Function ***def cat_matrices(mat1, mat2, axis=0):*** that concatenates two matrices along a specific axis:
