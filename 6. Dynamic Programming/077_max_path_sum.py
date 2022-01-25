import unittest

"""
--- Max path sum ---
Write a function, max_path_sum, that takes in a grid as an argument. The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. You may only travel through the grid by moving down or right.

You can assume that all numbers are non-negative.
"""


def max_path_sum(grid):
    rows = len(grid) - 1
    cols = len(grid[0]) - 1
    return calculate((0, 0), (rows, cols), grid, {})


def calculate(pos, end, grid, memo):

    row, col = pos
    max_row, max_col = end
    next_row = row + 1
    next_col = col + 1

    if pos in memo:
        return memo[pos]
    if pos == end:
        return grid[max_row][max_col]
    if row > max_row or col > max_col:
        return float("-inf")

    result = grid[row][col]

    down_result = calculate((next_row, col), end, grid, memo)
    right_result = calculate((row, next_col), end, grid, memo)

    memo[pos] = result + max(down_result, right_result)
    return memo[pos]


class Test(unittest.TestCase):

    def test_00(self):
        grid = [
            [1, 3, 12],
            [5, 1, 1],
            [3, 6, 1],
        ]
        max_path_sum(grid) == 18

    def test_01(self):
        grid = [
            [1, 2, 8, 1],
            [3, 1, 12, 10],
            [4, 0, 6, 3],
        ]
        max_path_sum(grid) == 36

    def test_02(self):
        grid = [
            [1, 2, 8, 1],
            [3, 10, 12, 10],
            [4, 0, 6, 3],
        ]
        max_path_sum(grid) == 39

    def test_03(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        max_path_sum(grid) == 27

    def test_04(self):
        grid = [
            [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
            [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        max_path_sum(grid) == 56


if __name__ == "__main__":
    unittest.main()
