"""
--- Post order ---
Write a function, post_order, that takes in the root of a binary tree. The function should return a list containing the post-ordered values of the tree.

Post-order traversal is when nodes are recursively visited in the order: left child, right child, self.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def post_order(root):
    values = []
    post_order_traversal(root, values)
    return values


def post_order_traversal(root, values):
    if not root:
        return
    post_order_traversal(root.left, values)
    post_order_traversal(root.right, values)
    values.append(root.val)


class Test(unittest.TestCase):
    def test_00(self):
        x = Node('x')
        y = Node('y')
        z = Node('z')

        x.left = y
        x.right = z

        #       x
        #    /    \
        #   y      z

        post_order(x) == ['y', 'z', 'x']

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
        c.left = f
        c.right = g

        #      a
        #    /    \
        #   b      c
        #  / \    / \
        # d   e  f   g

        post_order(a) == ['d', 'e', 'b', 'f', 'g', 'c', 'a']

    def test_02(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h

        #      a
        #    /    \
        #   b      c
        #  / \      \
        # d   e      f
        #    / \
        #    g  h

        post_order(a) == ['d', 'g', 'h', 'e', 'b', 'f', 'c', 'a']

    def test_03(self):
        l = Node('l')
        m = Node('m')
        n = Node('n')
        o = Node('o')
        p = Node('p')
        q = Node('q')
        r = Node('r')
        s = Node('s')
        t = Node('t')

        l.left = m
        l.right = n
        n.left = o
        n.right = p
        o.left = q
        o.right = r
        p.left = s
        p.right = t

        #        l
        #     /     \
        #    m       n
        #         /    \
        #         o     p
        #        / \   / \
        #       q   r s   t

        post_order(l) == ['m', 'q', 'r', 'o', 's', 't', 'p', 'n', 'l']

    def test_04(self):
        post_order(None) == []


if __name__ == "__main__":
    unittest.main()
