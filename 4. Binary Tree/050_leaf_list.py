"""
--- Leaf list ---
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.
"""
import unittest
from node import Node


def leaf_list(root):
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def leaf_list_rec(root):
    if not root:
        return []

    if not root.left and not root.right:
        return [root.val]

    return leaf_list_rec(root.left) + leaf_list_rec(root.right)


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

        assert leaf_list(a) == ['d', 'e', 'f']

    def test_01(self):
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

        assert leaf_list(a) == ['d', 'g', 'h']

    def test_02(self):
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        #        5
        #     /    \
        #    11    54
        #  /   \
        # 20   15
        #      / \
        #     1  3

        assert leaf_list(a) == [20, 1, 3, 54]

    def test_03(self):
        x = Node('x')

        #      x

        assert leaf_list(x) == ['x']

    def test_04(self):
        assert leaf_list(None) == []

    def test_05(self):
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

        assert leaf_list_rec(a) == ['d', 'e', 'f']

    def test_06(self):
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

        assert leaf_list_rec(a) == ['d', 'g', 'h']

    def test_07(self):
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        #        5
        #     /    \
        #    11    54
        #  /   \
        # 20   15
        #      / \
        #     1  3

        assert leaf_list_rec(a) == [20, 1, 3, 54]

    def test_08(self):
        x = Node('x')

        #      x

        assert leaf_list_rec(x) == ['x']

    def test_09(self):
        assert leaf_list_rec(None) == []


if __name__ == "__main__":
    unittest.main()
