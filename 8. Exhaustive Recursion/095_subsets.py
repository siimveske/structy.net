"""
--- Subsets ---
Write a function, subsets, that takes in a list as an argument. The function should return a 2D list where each sublist represents one of the possible subsets of the list.

The elements within the subsets and the subsets themselves may be returned in any order.

You may assume that the input list contains unique elements.
"""
import unittest


def subsets(elements):
    if len(elements) == 0:
        return [[]]

    first = elements[0]
    without_first = subsets(elements[1:])

    with_first = []
    for i in without_first:
        with_first.append([first, *i])

    return without_first + with_first


class Test(unittest.TestCase):
    def test_00(self):
        assert subsets(['a', 'b']) == [
            [],
            ['b'],
            ['a'],
            ['a', 'b']
        ]

    def test_01(self):
        assert subsets(['a', 'b', 'c']) == [
            [],
            ['c'],
            ['b'],
            ['b', 'c'],
            ['a'],
            ['a', 'c'],
            ['a', 'b'],
            ['a', 'b', 'c']
        ]

    def test_02(self):
        assert subsets(['x']) == [
            [],
            ['x']
        ]

    def test_03(self):
        assert subsets([]) == [
            []
        ]

    def test_04(self):
        assert subsets(['q', 'r', 's', 't']) == [
            [],
            ['t'],
            ['s'],
            ['s', 't'],
            ['r'],
            ['r', 't'],
            ['r', 's'],
            ['r', 's', 't'],
            ['q'],
            ['q', 't'],
            ['q', 's'],
            ['q', 's', 't'],
            ['q', 'r'],
            ['q', 'r', 't'],
            ['q', 'r', 's'],
            ['q', 'r', 's', 't']
        ]


if __name__ == "__main__":
    unittest.main()
