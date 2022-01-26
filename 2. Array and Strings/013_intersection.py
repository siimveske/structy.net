"""
--- Intersection ---
Write a function, intersection, that takes in two lists, a,b, as arguments. The function should return a new list containing elements that are in both of the two lists.

You may assume that each input list does not contain duplicate elements.
"""
import unittest


def intersection(a, b):

    memo = set(a)
    return [item for item in b if item in memo]


class Test(unittest.TestCase):
    def test_00(self):
        assert sorted(intersection([4, 2, 1, 6], [3, 6, 9, 2, 10])) == [2, 6]

    def test_01(self):
        assert sorted(intersection([2, 4, 6], [4, 2])) == [2, 4]

    def test_02(self):
        assert sorted(intersection([4, 2, 1], [1, 2, 4, 6])) == [1, 2, 4]

    def test_03(self):
        assert intersection([0, 1, 2], [10, 11]) == []

    def test_04(self):
        a = [i for i in range(0, 50000)]
        b = [i for i in range(0, 50000)]
        assert sorted(intersection(a, b)) == [i for i in range(0, 50000)]


if __name__ == "__main__":
    unittest.main()
