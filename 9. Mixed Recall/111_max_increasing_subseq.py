"""
--- Max increasing subseq ---
Write a function, max_increasing_subseq, that takes in a list of numbers as an argument. The function should return the length of the longest subsequence of strictly increasing numbers.

A subsequence of a list can be created by deleting any items of the list, while maintaining the relative order of items.
"""
import unittest


def max_increasing_subseq(numbers):
    memo = {}
    result = explore(numbers, 0, float('-inf'), memo)
    return result


def explore(numbers, idx, previous, memo):

    key = (idx, previous)

    if key in memo:
        return memo[key]
    if idx == len(numbers):
        return 0

    current = numbers[idx]
    options = []

    without_current = explore(numbers, idx + 1, previous, memo)
    options.append(without_current)
    if current > previous:
        with_current = 1 + explore(numbers, idx + 1, current, memo)
        options.append(with_current)

    memo[key] = max(options)
    return memo[key]


class Test(unittest.TestCase):

    def test_00(self):
        numbers = [4, 18, 20, 10, 12, 15, 19]
        assert max_increasing_subseq(numbers) == 5

    def test_01(self):
        numbers = [12, 9, 2, 5, 4, 32, 90, 20]
        assert max_increasing_subseq(numbers) == 4

    def test_02(self):
        numbers = [42, 50, 51, 60, 55, 70, 4, 5, 70]
        assert max_increasing_subseq(numbers) == 5

    def test_03(self):
        numbers = [7, 14, 10, 12]
        assert max_increasing_subseq(numbers) == 3

    def test_04(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        assert max_increasing_subseq(numbers) == 21

    def test_05(self):
        numbers = [
            1, 2, 3, 4, 5, 12, 6, 30, 7, 8, 9, 10, 11, 12, 13, 10, 18, 14, 15, 16, 17, 18, 19, 20, 21, 100,
            104,
        ]
        assert max_increasing_subseq(numbers) == 23

    def test_06(self):
        numbers = [
            1, 2, 300, 3, 4, 305, 5, 12, 6, 30, 7, 8, 9, 10, 10, 10, 15, 11, 12, 13, 10, 18, 14, 15, 16,
            17, 18, 19, 20, 21, 100, 101, 102, 103, 104, 105
        ]
        assert max_increasing_subseq(numbers) == 27


if __name__ == "__main__":
    unittest.main()
