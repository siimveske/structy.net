import unittest
from node import Node


def max_path_sum(root: Node):
    """Return the maximum sum of any root to leaf path
    within the tree (recursive depth first solution)"""

    if not root.left and not root.right:
        return root.val

    if not root.left:
        return root.val + max_path_sum(root.right)

    if not root.right:
        return root.val + max_path_sum(root.left)

    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))


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

        assert max_path_sum(a) == 18

    def test_01(self):
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

        assert max_path_sum(a) == 59

    def test_02(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(-13)
        g = Node(-1)
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
        # -3   0    -13
        #     /       \
        #    -1       -2

        assert max_path_sum(a) == -8

    def test_03(self):
        a = Node(42)
        # 42
        assert max_path_sum(a) == 42


if __name__ == "__main__":
    unittest.main()
