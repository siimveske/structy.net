"""
pair product
Write a function, pair_product, that takes in a list and a target product as arguments. The function should return a tuple containing a pair of indices whose elements multiply to the given target. The indices returned must be unique.

Be sure to return the indices, not the elements themselves.

There is guaranteed to be one such pair whose product is the target.
"""
import unittest


def pair_product(numbers, target_product):
    memo = {}
    for idx, number in enumerate(numbers):
        tmp = target_product // number
        if tmp in memo:
            return (memo[tmp], idx)
        memo[number] = idx


class Test(unittest.TestCase):
    def test_00(self):
        assert pair_product([3, 2, 5, 4, 1], 8) == (1, 3)

    def test_01(self):
        assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)

    def test_02(self):
        assert pair_product([4, 7, 9, 2, 5, 1], 5) == (4, 5)

    def test_03(self):
        assert pair_product([4, 7, 9, 2, 5, 1], 35) == (1, 4)

    def test_04(self):
        assert pair_product([3, 2, 5, 4, 1], 10) == (1, 2)

    def test_05(self):
        assert pair_product([4, 6, 8, 2], 16) == (2, 3)


if __name__ == "__main__":
    unittest.main()
