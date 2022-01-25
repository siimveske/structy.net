from re import I
import unittest

"""
--- Summing squares ---
Write a function, summing_squares, that takes a target number as an argument. The function should return the minimum number of perfect squares that sum to the target. A perfect square is a number of the form (i*i) where i >= 1.

For example: 1, 4, 9, 16 are perfect squares, but 8 is not perfect square.
"""


def perfect_squares(n):

    i = 1
    square = 0
    perfect_squares = []

    while square <= n:
        square = i * i
        if square <= n:
            perfect_squares.append(square)
            i += 1

    return perfect_squares


def summing_squares(n):
    squares = perfect_squares(n)
    return calculate(n, squares, {})


def calculate(n, squares, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0

    min_path = float("inf")
    for square in squares:
        if square <= n:
            result = 1 + calculate(n - square, squares, memo)
            min_path = min(result, min_path)
        else:
            break

    memo[n] = min_path
    return memo[n]


class Test(unittest.TestCase):

    def test_00(self):
        assert summing_squares(8) == 2

    def test_01(self):
        assert summing_squares(9) == 1

    def test_02(self):
        assert summing_squares(12) == 3

    def test_03(self):
        assert summing_squares(1) == 1

    def test_04(self):
        assert summing_squares(31) == 4

    def test_05(self):
        assert summing_squares(50) == 2

    def test_06(self):
        assert summing_squares(68) == 2

    def test_07(self):
        assert summing_squares(87) == 4


if __name__ == "__main__":
    unittest.main()
