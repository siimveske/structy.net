"""
--- Lefty nodes ---
Write a function, lefty_nodes, that takes in the root of a binary tree. The function should return a list containing the left-most value on every level of the tree. The list must be ordered in a top-down fashion where the root is the first item.
"""
import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lefty_nodes(root: Node):
    if not root:
        return []

    result = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()

        if len(result) == level:
            result.append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return result


class Test(unittest.TestCase):
    def test_00(self):
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

        assert lefty_nodes(a) == ['a', 'b', 'd', 'g']

    def test_01(self):
        u = Node('u')
        t = Node('t')
        s = Node('s')
        r = Node('r')
        q = Node('q')
        p = Node('p')

        u.left = t
        u.right = s
        s.right = r
        r.left = q
        r.right = p

        #     u
        #  /    \
        # t      s
        #         \
        #         r
        #        / \
        #        q  p

        assert lefty_nodes(u) == ['u', 't', 'r', 'q']

    def test_02(self):
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

        assert lefty_nodes(l) == ['l', 'm', 'o', 'q']

    def test_03(self):
        n = Node('n')
        y = Node('y')
        c = Node('c')

        n.left = y
        n.right = c

        #       n
        #     /   \
        #    y     c

        assert lefty_nodes(n) == ['n', 'y']

    def test_04(self):
        i = Node('i')
        n = Node('n')
        s = Node('s')
        t = Node('t')

        i.right = n
        n.left = s
        n.right = t

        #       i
        #        \
        #         n
        #        / \
        #       s   t

        assert lefty_nodes(i) == ['i', 'n', 's']

    def test_05(self):
        assert lefty_nodes(None) == []


if __name__ == "__main__":
    unittest.main()
