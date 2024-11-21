#!/usr/bin/python3
""" matrix (list of list of int): n x n 2D matrix to be rotated
None: The matrix is modified in-place """


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise in-place
    Args:
        matrix: n x n 2D matrix
    Returns:
        None (matrix is edited in-place)
    """

    n = len(matrix)

    # Step 1: Transpose the matrix (swap elements across main diagonal)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
