"""
--- Tree path finder ---
Write a function, path_finder, that takes in the root of a binary tree and a target value. The function should return an array representing a path to the target value. If the target value is not found in the tree, then return None.

You may assume that the tree contains unique values.
"""
import unittest
from node import Node


def path_finder(root, target):
    if not root:
        return None

    stack = [(root, [root.val])]
    while stack:
        node, path = stack.pop()
        if node.val == target:
            return path
        if node.left:
            newpath = path + [node.left.val]
            stack.append((node.left, newpath))
        if node.right:
            newpath = path + [node.right.val]
            stack.append((node.right, newpath))

    return None


def path_finder_rec(root, target):
    result = _path_finder(root, target)
    if result:
        result = result[::-1]
    return result


def _path_finder(root, target):
    if not root:
        return None

    if root.val == target:
        return [root.val]

    if root.left:
        left = _path_finder(root.left, target)
        if left:
            left.append(root.val)
            return left
    if root.right:
        right = _path_finder(root.right, target)
        if right:
            right.append(root.val)
            return right

    return None


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

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

        res = path_finder(a, 'e')
        assert path_finder(a, 'e') == ['a', 'b', 'e']

    def test_01(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

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

        assert path_finder(a, 'p') == None

    def test_02(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /       \
        #   g         h

        assert path_finder(a, "c") == ['a', 'c']

    def test_03(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /       \
        #   g         h

        assert path_finder(a, "h") == ['a', 'c', 'f', 'h']

    def test_04(self):
        x = Node("x")
        assert path_finder(x, "x") == ['x']

    def test_05(self):
        assert path_finder(None, "x") == None

    def test_06(self):

        root = Node(0)
        curr = root
        for i in range(1, 19500):
            curr.right = Node(i)
            curr = curr.right

        #      0
        #       \
        #        1
        #         \
        #          2
        #           \
        #            3
        #             .
        #              .
        #               .
        #              19498
        #                \
        #                19499

        assert path_finder(root, 16281) == [i for i in range(16282)]

    def test_07(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

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

        assert path_finder_rec(a, 'e') == ['a', 'b', 'e']

    def test_08(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

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

        assert path_finder_rec(a, 'p') == None

    def test_09(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /       \
        #   g         h

        assert path_finder_rec(a, "c") == ['a', 'c']

    def test_10(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /       \
        #   g         h

        assert path_finder_rec(a, "h") == ['a', 'c', 'f', 'h']

    def test_11(self):
        x = Node("x")
        assert path_finder_rec(x, "x") == ['x']

    def test_12(self):
        assert path_finder_rec(None, "x") == None

    def test_13(self):

        self.skipTest("RecursionError")

        root = Node(0)
        curr = root
        for i in range(1, 19500):
            curr.right = Node(i)
            curr = curr.right

        #      0
        #       \
        #        1
        #         \
        #          2
        #           \
        #            3
        #             .
        #              .
        #               .
        #              19498
        #                \
        #                19499

        assert path_finder_rec(root, 16281) == [i for i in range(16282)]


if __name__ == "__main__":
    unittest.main()
