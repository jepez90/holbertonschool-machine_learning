def matrix_transpose(matrix):
    """ returns the transpose of a 2D matrix, matrix """

    # generates the new matrix with the correct amount of rows
    transpose = [[] for col in matrix[0]]

    # run though the each row in the original matrix
    for row in matrix:

        # run through each element in each row
        for j in range(len(row)):

            # put each value of the column at end of the row
            # use j as row index in transpose and as column index in matrix
            transpose[j].append(row[j])

    return transpose
