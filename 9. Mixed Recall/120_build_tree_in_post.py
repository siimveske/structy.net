"""
--- Build tree in post ---
Write a function, build_tree_in_post, that takes in a list of in-ordered values and a list of post-ordered values for a binary tree. The function should build a binary tree that has the given in-order and post-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and postorder are unique.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def build_tree_in_post(in_order, post_order):
    if not post_order:
        return None

    value = post_order[-1]
    middle = in_order.index(value)
    left_in = in_order[:middle]
    right_in = in_order[middle + 1:]
    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in):-1]

    root = Node(value)
    root.left = build_tree_in_post(left_in, left_post)
    root.right = build_tree_in_post(right_in, right_post)

    return root


def post_order_traversal(root, values):
    if not root:
        return
    post_order_traversal(root.left, values)
    post_order_traversal(root.right, values)
    values.append(root.val)

    return values


def in_order_traversal(root, values):
    if not root:
        return
    in_order_traversal(root.left, values)
    values.append(root.val)
    in_order_traversal(root.right, values)

    return values


class Test(unittest.TestCase):
    def test_00(self):
        in_order = ['y', 'x', 'z']
        post_order = ['y', 'z', 'x']
        result = build_tree_in_post(in_order, post_order)

        #       x
        #    /    \
        #   y      z

        assert in_order_traversal(result, []) == in_order
        assert post_order_traversal(result, []) == post_order

    def test_01(self):
        in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
        post_order = ['d', 'e', 'b', 'f', 'g', 'c', 'a']
        result = build_tree_in_post(in_order, post_order)

        #      a
        #    /    \
        #   b      c
        #  / \    / \
        # d   e  f   g

        assert in_order_traversal(result, []) == in_order
        assert post_order_traversal(result, []) == post_order

    def test_02(self):
        in_order = ['d', 'b', 'g', 'e', 'h', 'a', 'c', 'f']
        post_order = ['d', 'g', 'h', 'e', 'b', 'f', 'c', 'a']
        result = build_tree_in_post(in_order, post_order)

        #      a
        #    /    \
        #   b      c
        #  / \      \
        # d   e      f
        #    / \
        #    g  h

        assert in_order_traversal(result, []) == in_order
        assert post_order_traversal(result, []) == post_order

    def test_03(self):
        in_order = ['m', 'n']
        post_order = ['m', 'n']
        result = build_tree_in_post(in_order, post_order)

        #       n
        #     /
        #    m

        assert in_order_traversal(result, []) == in_order
        assert post_order_traversal(result, []) == post_order

    def test_04(self):
        in_order = ['n', 'm']
        post_order = ['m', 'n']
        result = build_tree_in_post(in_order, post_order)

        #     n
        #      \
        #       m

        assert in_order_traversal(result, []) == in_order
        assert post_order_traversal(result, []) == post_order


if __name__ == "__main__":
    unittest.main()
