#!/usr/bin/python3


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int):
        2D grid where 0 represents water and 1 represents land.

    Returns:
        int: Perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Add 4 for each land cell
                perimeter += 4
                # Subtract 2 for each adjacent land cell
                if r > 0 and grid[r - 1][c] == 1:  # Check top
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:  # Check left
                    perimeter -= 2
    return perimeter
