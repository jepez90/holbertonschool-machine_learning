def add_matrices2D(mat1, mat2):
    """ adds two matrices element-wise """

    if matrix_shape(mat1) != matrix_shape(mat2):
        return None

    response = []

    # run trough first matrix and get each index and row
    for i, row1 in enumerate(mat1):
        row2 = mat2[i]
        # add each element of the both list or rows and generates a new row
        new_row = [row1[j] + row2[j] for j in range(len(row1))]
        response.append(new_row)
    return response


def matrix_shape(matrix):
    """ calculates the shape of a matrix: """
    if type(matrix) is list:
        response = [len(matrix)]
        response.extend(matrix_shape(matrix[0]))
        return response
    return []
