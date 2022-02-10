"""
--- Lowest common ancestor ---
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor(root, val1, val2):
    path1 = dfs(root, val1)
    path2 = dfs(root, val2)

    result = ''
    for item in list(zip(path1, path2)):
        a, b = item
        if a == b:
            result = a
        else:
            break

    return result


def dfs(root: Node, val: str):
    if not root:
        return ''
    if root.val == val:
        return root.val

    left = dfs(root.left, val)
    if left:
        return root.val + left

    right = dfs(root.right, val)
    if right:
        return root.val + right

    return ''


# example tree 1
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

# example tree 2
i = Node('i')
m = Node('m')
n = Node('n')
o = Node('o')
p = Node('p')
q = Node('q')
r = Node('r')
s = Node('s')
t = Node('t')

i.left = m
i.right = n
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


class Test(unittest.TestCase):

    def test_00(self):
        assert lowest_common_ancestor(a, 'd', 'h') == 'b'

    def test_01(self):
        assert lowest_common_ancestor(a, 'd', 'g') == 'b'

    def test_02(self):
        assert lowest_common_ancestor(a, 'g', 'c') == 'a'

    def test_03(self):
        assert lowest_common_ancestor(a, 'b', 'g') == 'b'

    def test_04(self):
        assert lowest_common_ancestor(a, 'f', 'c') == 'c'

    def test_05(self):
        assert lowest_common_ancestor(i, 'r', 'p') == 'n'

    def test_06(self):
        assert lowest_common_ancestor(i, 'm', 'o') == 'i'

    def test_07(self):
        assert lowest_common_ancestor(i, 't', 'q') == 'n'

    def test_08(self):
        assert lowest_common_ancestor(i, 's', 'p') == 'p'


if __name__ == "__main__":
    unittest.main()
