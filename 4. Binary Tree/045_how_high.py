"""
--- How high ---
Write a function, how_high, that takes in the root of a binary tree. The function should return a number representing the height of the tree.

The height of a binary tree is defined as the maximal number of edges from the root node to any leaf node.

If the tree is empty, return -1.
"""
import unittest
from node import Node


def how_high(node):
    if not node:
        return -1

    stack = [(node, 0)]
    tree_depth = 0

    while stack:
        current, count = stack.pop()
        if not current.left and not current.right:
            tree_depth = max(tree_depth, count)
        if current.left:
            stack.append((current.left, count + 1))
        if current.right:
            stack.append((current.right, count + 1))

    return tree_depth


def how_high_rec(node):
    if not node:
        return -1

    tree_depth = 0
    if node.left:
        left = 1 + how_high_rec(node.left)
        tree_depth = max(tree_depth, left)
    if node.right:
        right = 1 + how_high_rec(node.right)
        tree_depth = max(tree_depth, right)

    return tree_depth


class Test(unittest.TestCase):
    def test_00(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        assert how_high_rec(a) == 2

    def test_01(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        assert how_high_rec(a) == 3

    def test_02(self):
        a = Node('a')
        c = Node('c')

        a.right = c

        #      a
        #       \
        #        c

        assert how_high_rec(a) == 1

    def test_03(self):
        a = Node('a')
        assert how_high_rec(a) == 0

    def test_04(self):
        assert how_high_rec(None) == -1

    def test_05(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        assert how_high_rec(a) == 2

    def test_06(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        assert how_high_rec(a) == 3

    def test_07(self):
        a = Node('a')
        c = Node('c')

        a.right = c

        #      a
        #       \
        #        c

        assert how_high_rec(a) == 1

    def test_08(self):
        a = Node('a')
        assert how_high_rec(a) == 0

    def test_09(self):
        assert how_high_rec(None) == -1


if __name__ == "__main__":
    unittest.main()
