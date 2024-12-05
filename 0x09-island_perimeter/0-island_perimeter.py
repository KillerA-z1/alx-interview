#!/usr/bin/python3
def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    The grid is represented by a list of lists of integers where:
    - 0 represents water
    - 1 represents land

    Each cell is a square with a side length of 1. The grid is completely
    surrounded by water, and there is exactly one island (or none).
    The island doesn't have "lakes" (water inside that isn't connected to the
    water around the island).

    Args:
        grid (List[List[int]]):list of lists of integers representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    """Returns the perimeter of the island described in grid."""
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check the cell above
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check the cell below
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check the cell to the left
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
