import unittest

"""
--- Min change ---
Write a function min_change that takes in an amount and a list of coins. The function should return the minimum number of coins required to create the amount. You may use each coin as many times as necessary.

If it is not possible to create the amount, then return -1.
"""


def min_change(amount, coins):
    res = calculate(amount, coins, {})
    if res == float("inf"):
        return -1
    else:
        return res


def calculate(amount, coins, memo):
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    min_cost = float("inf")
    for coin in coins:
        cost = 1 + calculate(amount - coin, coins, memo)
        if cost < min_cost:
            min_cost = cost

    memo[amount] = min_cost
    return min_cost


class Test(unittest.TestCase):

    def test_00(self):
        assert min_change(8, [1, 5, 4, 12]) == 2

    def test_01(self):
        assert min_change(13, [1, 9, 5, 14, 30]) == 5

    def test_02(self):
        assert min_change(23, [2, 5, 7]) == 4

    def test_03(self):
        assert min_change(102, [1, 5, 10, 25]) == 6

    def test_04(self):
        assert min_change(200, [1, 5, 10, 25]) == 8

    def test_05(self):
        assert min_change(2017, [4, 2, 10]) == -1

    def test_06(self):
        assert min_change(271, [10, 8, 265, 24]) == -1

    def test_07(self):
        assert min_change(0, [4, 2, 10]) == 0

    def test_08(self):
        assert min_change(0, []) == 0


if __name__ == "__main__":
    unittest.main()
