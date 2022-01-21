import unittest
from node import Node
from collections import deque


def breadth_first_values(root: Node):
    """Find btree values iteratively"""
    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        values.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return values


def rbreadth_first_values(root: Node):
    """Find btree values recursively"""
    if root is None:
        return []

    lvalues = rbreadth_first_values(root.left)
    rvalues = rbreadth_first_values(root.right)

    return [root.val, *lvalues, *rvalues]


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

        values = breadth_first_values(a)
        assert values == ["a", "b", "c", "d", "e", "f"]

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

        values = breadth_first_values(a)
        assert values == ["a", "b", "c", "d", "e", "f", "g", "h"]

    def test_02(self):
        a = Node("a")
        #     a
        values = breadth_first_values(a)
        assert values == ["a"]

    def test_03(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        x = Node("x")

        a.right = b
        b.left = c
        c.left = x
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #    /  \
        #   x    d
        #         \
        #          e

        values = breadth_first_values(a)
        assert values == ["a", "b", "c", "x", "d", "e"]

    def test_04(self):
        values = breadth_first_values(None)
        assert values == []


if __name__ == "__main__":
    unittest.main()
