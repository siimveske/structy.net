"""
--- Bottom right value ---
Write a function, bottom_right_value, that takes in the root of a binary tree. The function should return the right-most value in the bottom-most level of the tree.

You may assume that the input tree is non-empty.
"""


import unittest
from node import Node
from collections import deque

# def bottom_right_value(root):

#     stack = [(root, ["1"])]
#     result = ''
#     max_val = float("-inf")

#     while stack:
#         node, val = stack.pop()
#         if node.left:
#             stack.append((node.left, [*val, "0"]))
#         if node.right:
#             stack.append((node.right, [*val, "1"]))
#         if not node.left and not node.right:
#             bin_value = ''.join(val)
#             dec_value = int(bin_value, 2)
#             if dec_value > max_val:
#                 max_val = dec_value
#                 result = node.val

#     return result


def bottom_right_value(root):
    '''Use breath first algorithm to find bottom most right value'''

    stack = deque([root])
    while stack:
        node = stack.popleft()
        if not node.left and not node.right and not stack:
            return node.val
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(3)
        b = Node(11)
        c = Node(10)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      3
        #    /   \
        #   11    10
        #  / \      \
        # 4   -2     1

        assert bottom_right_value(a) == 1

    def test_01(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4    -13
        #      / \
        #    -2   6

        assert bottom_right_value(a) == 6

    def test_02(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)
        i = Node(7)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     / \    /
        #    -2  6  7

        assert bottom_right_value(a) == 7

    def test_03(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')

        a.left = b
        a.right = c
        b.right = d
        d.left = e
        e.right = f

        #      a
        #    /   \
        #   b     c
        #    \
        #     d
        #    /
        #   e
        #    \
        #     f

        assert bottom_right_value(a) == 'f'

    def test_04(self):
        a = Node(42)
        assert bottom_right_value(a) == 42


if __name__ == "__main__":
    unittest.main()
