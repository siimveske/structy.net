"""
--- Tree levels ---
Write a function, tree_levels, that takes in the root of a binary tree. The function should return a 2-Dimensional list where each sublist represents a level of the tree.
"""

import unittest
from node import Node
from collections import deque


def tree_levels(root):
    if not root:
        return []

    queue = deque([(root, 0)])
    levels = []

    while queue:
        node, level = queue.popleft()

        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return levels


def tree_levels_rec(root: Node):
    levels = []
    _tree_levels_rec(root, levels, 0)
    return levels


def _tree_levels_rec(root: Node, levels: list, level: int):
    if not root:
        return

    if len(levels) == level:
        levels.append([])
    levels[level].append(root.val)

    _tree_levels_rec(root.left, levels, level + 1)
    _tree_levels_rec(root.right, levels, level + 1)


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

        assert tree_levels(a) == [
            ['a'],
            ['b', 'c'],
            ['d', 'e', 'f']
        ]

    def test_01(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')
        i = Node('i')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
        #     b      c
        #   /  \      \
        #  d    e      f
        #      / \    /
        #     g  h   i

        assert tree_levels(a) == [
            ['a'],
            ['b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]

    def test_02(self):
        q = Node('q')
        r = Node('r')
        s = Node('s')
        t = Node('t')
        u = Node('u')
        v = Node('v')

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
        #   r     s
        #    \
        #     t
        #    /
        #   u
        #  /
        # v

        assert tree_levels(q) == [
            ['q'],
            ['r', 's'],
            ['t'],
            ['u'],
            ['v']
        ]

    def test_03(self):
        assert tree_levels(None) == []

    def test_04(self):
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

        assert tree_levels_rec(a) == [
            ['a'],
            ['b', 'c'],
            ['d', 'e', 'f']
        ]

    def test_05(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')
        i = Node('i')

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
        #     b      c
        #   /  \      \
        #  d    e      f
        #      / \    /
        #     g  h   i

        assert tree_levels_rec(a) == [
            ['a'],
            ['b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i']
        ]

    def test_06(self):
        q = Node('q')
        r = Node('r')
        s = Node('s')
        t = Node('t')
        u = Node('u')
        v = Node('v')

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
        #   r     s
        #    \
        #     t
        #    /
        #   u
        #  /
        # v

        assert tree_levels_rec(q) == [
            ['q'],
            ['r', 's'],
            ['t'],
            ['u'],
            ['v']
        ]

    def test_07(self):
        assert tree_levels_rec(None) == []


if __name__ == "__main__":
    unittest.main()
