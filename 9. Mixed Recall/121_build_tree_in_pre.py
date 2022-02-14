"""
--- Build tree in pre ---
Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and preorder are unique.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_in_pre(in_order, pre_order):
    if not pre_order:
        return None

    value = pre_order[0]
    middle = in_order.index(value)
    left_in = in_order[:middle]
    right_in = in_order[middle + 1:]
    left_pre = pre_order[1:len(left_in) + 1]
    right_pre = pre_order[len(left_in) + 1:]

    root = Node(value)
    root.left = build_tree_in_pre(left_in, left_pre)
    root.right = build_tree_in_pre(right_in, right_pre)

    return root


def in_order_traversal(root, values):
    if not root:
        return
    in_order_traversal(root.left, values)
    values.append(root.val)
    in_order_traversal(root.right, values)

    return values


def pre_order_traversal(root, values):
    if not root:
        return
    values.append(root.val)
    pre_order_traversal(root.left, values)
    pre_order_traversal(root.right, values)

    return values


class Test(unittest.TestCase):
    def test_00(self):
        in_order = ['z', 'y', 'x']
        pre_order = ['y', 'z', 'x']
        result = build_tree_in_pre(in_order, pre_order)

        #       y
        #    /    \
        #   z      x

        assert in_order_traversal(result, []) == in_order
        assert pre_order_traversal(result, []) == pre_order

    def test_01(self):
        in_order = ['y', 'z', 'x']
        pre_order = ['y', 'x', 'z']
        result = build_tree_in_pre(in_order, pre_order)

        #       y
        #        \
        #         x
        #        /
        #       z

        assert in_order_traversal(result, []) == in_order
        assert pre_order_traversal(result, []) == pre_order

    def test_02(self):
        in_order = ['d', 'b', 'g', 'e', 'h', 'a', 'c', 'f']
        pre_order = ['a', 'b', 'd', 'e', 'g', 'h', 'c', 'f']
        result = build_tree_in_pre(in_order, pre_order)

        #       a
        #    /    \
        #   b      c
        #  / \      \
        # d   e      f
        #    / \
        #    g  h

        assert in_order_traversal(result, []) == in_order
        assert pre_order_traversal(result, []) == pre_order

    def test_03(self):
        in_order = ['t', 'u', 's', 'q', 'r', 'p']
        pre_order = ['u', 't', 's', 'r', 'q', 'p']
        result = build_tree_in_pre(in_order, pre_order)

        #     u
        #  /    \
        # t      s
        #         \
        #         r
        #        / \
        #        q  p

        assert in_order_traversal(result, []) == in_order
        assert pre_order_traversal(result, []) == pre_order

    def test_04(self):
        in_order = ['m', 'l', 'q', 'o', 'r', 'n', 's', 'p', 't']
        pre_order = ['l', 'm', 'n', 'o', 'q', 'r', 'p', 's', 't']
        result = build_tree_in_pre(in_order, pre_order)

        #        l
        #     /     \
        #    m       n
        #         /    \
        #         o     p
        #        / \   / \
        #       q   r s   t

        assert in_order_traversal(result, []) == in_order
        assert pre_order_traversal(result, []) == pre_order


if __name__ == "__main__":
    unittest.main()
