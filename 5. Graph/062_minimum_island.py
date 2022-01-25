import unittest

"""
--- Minimum island ---
Write a function, minimum_island, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the size of the smallest island. An island is a vertically or horizontally connected region of land.

You may assume that the grid contains at least one island
"""


def explore(grid, row, col, visited):
    row_inbound = 0 <= row < len(grid)
    col_inboud = 0 <= col < len(grid[0])

    if not row_inbound or not col_inboud:
        return 0
    if grid[row][col] == 'W':
        return 0
    if (row, col) in visited:
        return 0

    visited.add((row, col))

    size = 1
    size += explore(grid, row - 1, col, visited)
    size += explore(grid, row + 1, col, visited)
    size += explore(grid, row, col - 1, visited)
    size += explore(grid, row, col + 1, visited)

    return size


def minimum_island(grid):
    """Return the size of the smallest island"""

    visited = set()
    result = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            island_size = explore(grid, row, col, visited)
            if island_size != 0 and island_size < result:
                result = island_size

    return result


class Test(unittest.TestCase):
    def test_00(self):
        grid = [
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'L', 'W'],
            ['W', 'W', 'L', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['L', 'L', 'W', 'W', 'W'],
        ]
        assert minimum_island(grid) == 2

    def test_01(self):
        grid = [
            ['L', 'W', 'W', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['W', 'L', 'W', 'L', 'W'],
            ['W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'L', 'L', 'L'],
        ]
        assert minimum_island(grid) == 1

    def test_02(self):
        grid = [
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
        ]
        assert minimum_island(grid) == 9

    def test_03(self):
        grid = [
            ['W', 'W'],
            ['L', 'L'],
            ['W', 'W'],
            ['W', 'L'],
        ]
        assert minimum_island(grid) == 1


if __name__ == '__main__':
    unittest.main()
