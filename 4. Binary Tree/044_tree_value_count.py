"""
--- Tree value count ---
Write a function, tree_value_count, that takes in the root of a binary tree and a target value. The function should return the number of times that the target occurs in the tree.
"""

import unittest
from node import Node


def tree_value_count_rec(root: Node, target: int):
    if not root:
        return 0

    result = 0
    if root.val == target:
        result += 1

    result += tree_value_count_rec(root.left, target)
    result += tree_value_count_rec(root.right, target)

    return result


def tree_value_count(root: Node, target: int):
    if not root:
        return 0

    result = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val == target:
            result += 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4   6     12

        assert tree_value_count(a, 6) == 3

    def test_01(self):
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4  6     12

        assert tree_value_count(a, 12) == 2

    def test_02(self):
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        assert tree_value_count(a, 1) == 4

    def test_03(self):
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        assert tree_value_count(a, 9) == 0

    def test_04(self):
        assert tree_value_count(None, 42) == 0

    def test_05(self):
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4   6     12

        assert tree_value_count_rec(a, 6) == 3

    def test_06(self):
        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4  6     12

        assert tree_value_count_rec(a, 12) == 2

    def test_07(self):
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        assert tree_value_count_rec(a, 1) == 4

    def test_08(self):
        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        assert tree_value_count_rec(a, 9) == 0

    def test_09(self):
        assert tree_value_count_rec(None, 42) == 0


if __name__ == "__main__":
    unittest.main()
