import unittest

"""
--- Array stepper ---
Write a function, array_stepper, that takes in a list of numbers as an argument. You start at the first position of the list. The function should return a boolean indicating whether or not it is possible to reach the last position of the list. When situated at some position of the list, you may take a maximum number of steps based on the number at that position.

For example, given:

    idx =  0  1  2  3  4  5
numbers = [2, 4, 2, 0, 0, 1]

The answer is True.
We start at idx 0, we could take 1 step or 2 steps forward.
The correct choice is to take 1 step to idx 1.
Then take 4 steps forward to the end at idx 5.
"""


def array_stepper(numbers):
    return calculate(numbers, 0, {})


def calculate(numbers, idx, memo):
    if idx in memo:
        return memo[idx]
    if idx >= len(numbers):
        return False
    if idx == len(numbers) - 1:
        return True
    if numbers[idx] == 0:
        return False

    for i in range(1, numbers[idx] + 1):
        if calculate(numbers, idx + i, memo):
            memo[idx] = True
            return memo[idx]

    memo[idx] = False
    return memo[idx]


class Test(unittest.TestCase):

    def test_00(self):
        assert array_stepper([2, 4, 2, 0, 0, 1]) == True

    def test_01(self):
        assert array_stepper([2, 3, 2, 0, 0, 1]) == False

    def test_02(self):
        assert array_stepper([3, 1, 3, 1, 0, 1]) == True

    def test_03(self):
        assert array_stepper([4, 1, 5, 1, 1, 1, 0, 4]) == True

    def test_04(self):
        assert array_stepper([4, 1, 2, 1, 1, 1, 0, 4]) == False

    def test_05(self):
        assert array_stepper([1, 1, 1, 1, 1, 0]) == True

    def test_06(self):
        assert array_stepper([1, 1, 1, 1, 0, 0]) == False

    def test_07(self):
        assert array_stepper([
            31, 30, 29, 28, 27,
            26, 25, 24, 23, 22,
            21, 20, 19, 18, 17,
            16, 15, 14, 13, 12,
            11, 10, 9, 8, 7, 6,
            5, 3, 2, 1, 0, 0, 0
        ]) == False


if __name__ == "__main__":
    unittest.main()
