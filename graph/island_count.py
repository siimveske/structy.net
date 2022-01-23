'''
https://structy.net/problems/island-count
https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=5976s
'''


import unittest


def explore(grid, row, col, visited):
    rowInbound = 0 <= row < len(grid)
    colInboud = 0 <= col < len(grid[0])

    if not rowInbound or not colInboud:
        return False
    if grid[row][col] == 'W':
        return False
    if (row, col) in visited:
        return False

    visited.add((row, col))

    explore(grid, row - 1, col, visited)
    explore(grid, row + 1, col, visited)
    explore(grid, row, col - 1, visited)
    explore(grid, row, col + 1, visited)

    return True


def island_count(grid):
    visited = set()
    island_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                island_count += 1
    return island_count


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
        assert island_count(grid) == 3

    def test_01(self):
        grid = [
            ['L', 'W', 'W', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['W', 'L', 'W', 'L', 'W'],
            ['W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'L', 'L', 'L'],
        ]
        assert island_count(grid) == 4

    def test_02(self):
        grid = [
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
        ]
        assert island_count(grid) == 1

    def test_03(self):
        grid = [
            ['W', 'W'],
            ['W', 'W'],
            ['W', 'W'],
        ]
        assert island_count(grid) == 0


if __name__ == '__main__':
    unittest.main()
