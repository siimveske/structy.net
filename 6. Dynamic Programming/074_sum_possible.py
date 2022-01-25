import unittest

"""
--- Sum possible ---
Write a function sum_possible that takes in an amount and a list of positive numbers. The function should return a boolean indicating whether or not it is possible to create the amount by summing numbers of the list. You may reuse numbers of the list as many times as necessary.

You may assume that the target amount is non-negative.
"""


def sum_possible(amount, numbers):
    return calculate(amount, numbers, {})


def calculate(amount, numbers, memo):
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return True
    if amount < 0:
        return False
    if not numbers:
        return False

    for number in numbers:
        if calculate(amount - number, numbers, memo):
            memo[amount] = True
            return True
        else:
            memo[amount] = False

    return False


class Test(unittest.TestCase):
    def test_00(self):
        assert sum_possible(8, [5, 12, 4]) == True

    def test_01(self):
        assert sum_possible(15, [6, 2, 10, 19]) == False

    def test_02(self):
        assert sum_possible(13, [6, 2, 1]) == True

    def test_03(self):
        assert sum_possible(103, [6, 20, 1]) == True

    def test_04(self):
        assert sum_possible(12, []) == False

    def test_05(self):
        assert sum_possible(12, [12]) == True

    def test_06(self):
        assert sum_possible(0, []) == True

    def test_07(self):
        assert sum_possible(271, [10, 8, 265, 24]) == False

    def test_08(self):
        assert sum_possible(2017, [4, 2, 10]) == False

    def test_09(self):
        assert sum_possible(13, [3, 5]) == True


if __name__ == "__main__":
    unittest.main()
