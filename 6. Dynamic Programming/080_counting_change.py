import unittest

"""
--- Counting change ---
Write a function, counting_change, that takes in an amount and a list of coins. The function should return the number of different ways it is possible to make change for the given amount using the coins. You may reuse a coin as many times as necessary.

For example,
counting_change(4, [1,2,3]) -> 4
There are four different ways to make an amount of 4:

1. 1 + 1 + 1 + 1
2. 1 + 1 + 2
3. 1 + 3
4. 2 + 2
"""


def counting_change(amount, coins):
    return calculate(amount, coins, 0, {})


def calculate(amount, coins, coin_index, memo):

    key = (amount, coin_index)

    if key in memo:
        return memo[key]
    if amount == 0:
        return 1
    if coin_index == len(coins):
        return 0

    total = 0
    coin = coins[coin_index]
    for qty in range(0, (amount // coin) + 1):
        new_amount = amount - (coin * qty)
        total += calculate(new_amount, coins, coin_index + 1, memo)

    memo[key] = total
    return memo[key]


class Test(unittest.TestCase):

    def test_00(self):
        assert counting_change(4, [1, 2, 3]) == 4

    def test_01(self):
        assert counting_change(8, [1, 2, 3]) == 10

    def test_02(self):
        assert counting_change(24, [5, 7, 3]) == 5

    def test_03(self):
        assert counting_change(13, [2, 6, 12, 10]) == 0

    def test_04(self):
        assert counting_change(512, [1, 5, 10, 25]) == 20119

    def test_05(self):
        assert counting_change(1000, [1, 5, 10, 25]) == 142511

    def test_06(self):
        assert counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1525987916


if __name__ == "__main__":
    unittest.main()
