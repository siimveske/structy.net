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

    value = post_order.pop()
    middle = in_order.index(value)
    left_in = in_order[:middle]
    right_in = in_order[middle + 1:]
    left_post = post_order[:len(left_in)]
    right_post = post_order[len(left_in):]

    root = Node(value)
    root.left = build_tree_in_post(left_in, left_post)
    root.right = build_tree_in_post(right_in, right_post)

    return root


class Test(unittest.TestCase):
    # def test_00(self):
    #     result = build_tree_in_post(
    #         ['y', 'x', 'z'],
    #         ['y', 'z', 'x']
    #     )
    #     print()
    #     #       x
    #     #    /    \
    #     #   y      z

    def test_01(self):
        result = build_tree_in_post(
            ['d', 'b', 'e', 'a', 'f', 'c', 'g'],
            ['d', 'e', 'b', 'f', 'g', 'c', 'a']
        )
        print()
        #      a
        #    /    \
        #   b      c
        #  / \    / \
        # d   e  f   g

    # def test_02(self):
    #     result = build_tree_in_post(
    #         ['d', 'b', 'g', 'e', 'h', 'a', 'c', 'f'],
    #         ['d', 'g', 'h', 'e', 'b', 'f', 'c', 'a']
    #     )
    #     #      a
    #     #    /    \
    #     #   b      c
    #     #  / \      \
    #     # d   e      f
    #     #    / \
    #     #    g  h

    # def test_03(self):
    #     result = build_tree_in_post(
    #         ['m', 'n'],
    #         ['m', 'n']
    #     )
    #     #       n
    #     #     /
    #     #    m

    # def test_04(self):
    #     result = build_tree_in_post(
    #         ['n', 'm'],
    #         ['m', 'n']
    #     )
    #     #     n
    #     #      \
    #     #       m


if __name__ == "__main__":
    unittest.main()
