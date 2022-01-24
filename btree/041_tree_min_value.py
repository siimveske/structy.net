import unittest
from node import Node

"""
--- Tree min value ---
Write a function, tree_min_value, that takes in the root of a binary tree that contains number values. The function should return the minimum value within the tree.

You may assume that the input tree is non-empty.
"""


def tree_min_value(root: Node):
    """Return the minimum value within the tree
    (iterative depth first solution)"""

    if not root:
        return float("inf")

    stack = [root]
    minimum = float("inf")

    while stack:
        node = stack.pop()
        if node.val < minimum:
            minimum = node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return minimum


def rtree_min_value(root: Node):
    """return the minimum value within the tree
    (recursive depth first solution)"""

    if not root:
        return float("inf")

    return min([root.val, rtree_min_value(root.left), rtree_min_value(root.right)])


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

        assert tree_min_value(a) == -2

    def test_01(self):
        a = Node(5)
        b = Node(11)
        c = Node(3)
        d = Node(4)
        e = Node(14)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       5
        #    /    \
        #   11     3
        #  / \      \
        # 4   14     12

        assert tree_min_value(a) == 3

    def test_02(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     /       \
        #    -2       -2

        tree_min_value(a) == -13

    def test_03(self):
        a = Node(42)
        # 42
        assert tree_min_value(a) == 42

    def test_04(self):
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

        assert rtree_min_value(a) == -2

    def test_05(self):
        a = Node(5)
        b = Node(11)
        c = Node(3)
        d = Node(4)
        e = Node(14)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       5
        #    /    \
        #   11     3
        #  / \      \
        # 4   14     12

        assert rtree_min_value(a) == 3

    def test_06(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     /       \
        #    -2       -2

        rtree_min_value(a) == -13

    def test_07(self):
        a = Node(42)
        # 42
        assert rtree_min_value(a) == 42


if __name__ == "__main__":
    unittest.main()
