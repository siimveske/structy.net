"""
--- Closest carrot ---
Write a function, closest_carrot, that takes in a grid, a starting row, and a starting column. In the grid, 'X's are walls, 'O's are open spaces, and 'C's are carrots. The function should return a number representing the length of the shortest path from the starting position to a carrot. You may move up, down, left, or right, but cannot pass through walls (X). If there is no possible path to a carrot, then return -1.
"""
import unittest
from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    visited = set()
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        row_inbounds = 0 <= row < len(grid)
        col_inbounds = 0 <= col < len(grid[0])

        if not row_inbounds or not col_inbounds:
            continue
        if grid[row][col] == 'X':
            continue
        if (row, col) in visited:
            continue
        if grid[row][col] == "C":
            return distance

        visited.add((row, col))

        queue.append((row + 1, col, distance + 1))
        queue.append((row - 1, col, distance + 1))
        queue.append((row, col + 1, distance + 1))
        queue.append((row, col - 1, distance + 1))

    return -1


class Test(unittest.TestCase):
    def test_00(self):
        grid = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['O', 'X', 'C', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['C', 'O', 'O', 'O', 'O'],
        ]

        assert closest_carrot(grid, 1, 2) == 4

    def test_01(self):
        grid = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['O', 'X', 'C', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['C', 'O', 'O', 'O', 'O'],
        ]

        assert closest_carrot(grid, 0, 0) == 5

    def test_02(self):
        grid = [
            ['O', 'O', 'X', 'X', 'X'],
            ['O', 'X', 'X', 'X', 'C'],
            ['O', 'X', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'C', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O'],
        ]

        assert closest_carrot(grid, 3, 4) == 9

    def test_03(self):
        grid = [
            ['O', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'O'],
            ['O', 'X', 'C', 'C', 'O'],
        ]

        assert closest_carrot(grid, 1, 4) == 2

    def test_04(self):
        grid = [
            ['O', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'O'],
            ['O', 'X', 'C', 'C', 'O'],
        ]

        assert closest_carrot(grid, 2, 0) == -1

    def test_05(self):
        grid = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
        ]

        assert closest_carrot(grid, 0, 0) == -1


if __name__ == "__main__":
    unittest.main()
