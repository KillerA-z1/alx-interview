#!/usr/bin/python3
"""Generate Pascal's Triangle up to the nth row."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]:list of lists of integers representing Pascal Triangle.
                         Each inner list represents a row of Pascal's Triangle.
                         If n <= 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        if i == 0:
            row = [1]
        else:
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
        triangle.append(row)

    return triangle
