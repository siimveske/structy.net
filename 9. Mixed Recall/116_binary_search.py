"""
--- Binary search ---
Write a function, binary_search, that takes in a sorted list of numbers and a target. The function should return the index where the target can be found within the list. If the target is not found in the list, then return -1.

You may assume that the input array contains unique numbers sorted in increasing order.

Your function must implement the binary search algorithm.
"""
import unittest


def binary_search(numbers, target):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] == target:
            return mid
        if target < numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


class Test(unittest.TestCase):
    def test_00(self):
        assert binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8], 6) == 6

    def test_01(self):
        assert binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 27) == -1

    def test_02(self):
        assert binary_search([0, 6, 8, 12, 16, 19, 20, 28], 8) == 2

    def test_03(self):
        assert binary_search([0, 6, 8, 12, 16, 19, 20, 24, 28], 28) == 8

    def test_04(self):
        assert binary_search([7, 9], 7) == 0

    def test_05(self):
        assert binary_search([7, 9], 9) == 1

    def test_06(self):
        assert binary_search([7, 9], 12) == -1

    def test_07(self):
        assert binary_search([7], 7) == 0

    def test_08(self):
        assert binary_search([], 7) == -1


if __name__ == "__main__":
    unittest.main()
