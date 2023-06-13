#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    rows = len(matrix)  # no. of rows/length of the matrix
    columns = len(matrix[0])  # length of the first row in matrix

    if matrix == [[]]:
        print()

    for j in range(rows):
        for k in range(columns):
            if k == columns - 1:
                print("{:d}".format(matrix[j][k]))
            else:
                print("{:d}".format(matrix[j][k]), end=" ")
