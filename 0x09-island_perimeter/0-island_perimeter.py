#!/usr/bin/python3
''' Island Perimeter Interview Question'''


def island_perimeter(grid):
    ''' Returns the perimeter of the island described in `grid` '''

    if not grid:
        return 0
    pr = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    pr += 1
                if col == 0 or grid[row][col - 1] == 0:
                    pr += 1
                if row == len(grid) - 1 or grid[row + 1][col] == 0:
                    pr += 1
                if col == len(grid[row]) - 1 or grid[row][col + 1] == 0:
                    pr += 1
    return pr
