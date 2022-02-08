"""
--- Create combinations ---
Write a function, create_combinations, that takes in a list and a length as arguments. The function should return a 2D list representing all of the combinations of the specifized length.

The items within the combinations and the combinations themselves may be returned in any order.

You may assume that the input list contains unique elements and 1 <= k <= len(items).
"""
import unittest


# def create_combinations(items, k):
#     combinations = [[]]
#     for item in items:
#         tmp = []
#         for subset in combinations:
#             tmp.append(subset)
#             tmp.append(subset + [item])
#         combinations = tmp

#     result = [i for i in combinations if len(i) == k]
#     return result

def create_combinations(items, k):
    if k == 0:
        return [[]]
    if k > len(items):
        return []

    first = items[0]
    rest = items[1:]

    with_first = create_combinations(rest, k - 1)
    with_first = [[first] + i for i in with_first]
    without_first = create_combinations(rest, k)

    result = with_first + without_first
    return result


class Test(unittest.TestCase):
    def test_00(self):
        create_combinations(["a", "b", "c"], 2) == [
            ['a', 'b'],
            ['a', 'c'],
            ['b', 'c']
        ]

    def test_01(self):
        create_combinations(["q", "r", "s", "t"], 2) == [
            ['q', 'r'],
            ['q', 's'],
            ['q', 't'],
            ['r', 's'],
            ['r', 't'],
            ['s', 't']
        ]

    def test_02(self):
        create_combinations(['q', 'r', 's', 't'], 3) == [
            ['q', 'r', 's'],
            ['q', 'r', 't'],
            ['q', 's', 't'],
            ['r', 's', 't']
        ]

    def test_03(self):
        create_combinations([1, 28, 94], 3) == [
            [1, 28, 94]
        ]


if __name__ == "__main__":
    unittest.main()
