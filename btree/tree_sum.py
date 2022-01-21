import unittest
from node import Node


def tree_sum(root: Node):
    """Find sum of btree values iteratively (depth first solution)"""
    if root is None:
        return 0

    total = 0
    stack = [root]

    while stack:
        node = stack.pop()
        total += node.val
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return total


def rtree_sum(root: Node):
    """Find btree values recursively"""
    if root is None:
        return 0

    total = root.val

    total += rtree_sum(root.left)
    total += rtree_sum(root.right)

    return total


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

        result = tree_sum(a)
        assert result == 21

    def test_01(self):
        a = Node(1)
        b = Node(6)
        c = Node(0)
        d = Node(3)
        e = Node(-6)
        f = Node(2)
        g = Node(2)
        h = Node(2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      1
        #    /   \
        #   6     0
        #  / \     \
        # 3   -6    2
        #    /       \
        #   2         2

        result = tree_sum(a)
        assert result == 10

    def test_02(self):
        result = tree_sum(None)
        assert result == 0

    def test_03(self):
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

        result = rtree_sum(a)
        assert result == 21

    def test_04(self):
        a = Node(1)
        b = Node(6)
        c = Node(0)
        d = Node(3)
        e = Node(-6)
        f = Node(2)
        g = Node(2)
        h = Node(2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      1
        #    /   \
        #   6     0
        #  / \     \
        # 3   -6    2
        #    /       \
        #   2         2

        result = rtree_sum(a)
        assert result == 10

    def test_05(self):
        result = rtree_sum(None)
        assert result == 0


if __name__ == "__main__":
    unittest.main()
