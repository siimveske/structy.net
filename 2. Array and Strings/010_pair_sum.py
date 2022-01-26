"""
--- Pair sum ---
Write a function, pair_sum, that takes in a list and a target sum as arguments. The function should return a tuple containing a pair of indices whose elements sum to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair that sums to the target.
"""
import unittest


def pair_sum(numbers, target_sum):
    previous = {}
    for idx, num in enumerate(numbers):
        complement = target_sum - num
        if complement in previous:
            return (previous[complement], idx)
        else:
            previous[num] = idx


class Test(unittest.TestCase):
    def test_00(self):
        assert pair_sum([3, 2, 5, 4, 1], 8) == (0, 2)

    def test_01(self):
        assert pair_sum([4, 7, 9, 2, 5, 1], 5) == (0, 5)

    def test_02(self):
        assert pair_sum([4, 7, 9, 2, 5, 1], 3) == (3, 5)

    def test_03(self):
        assert pair_sum([1, 6, 7, 2], 13) == (1, 2)

    def test_04(self):
        assert pair_sum([9, 9], 18) == (0, 1)

    def test_05(self):
        assert pair_sum([6, 4, 2, 8], 12) == (1, 3)


if __name__ == "__main__":
    unittest.main()
