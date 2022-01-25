"""
lowest common ancestor
Write a function, lowest_common_ancestor, that takes in the root of a binary tree and two values. The function should return the value of the lowest common ancestor of the two values in the tree.

You may assume that the tree values are unique and the tree is non-empty.

Note that a node may be considered an ancestor of itself.

example tree
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
test_00
lowest_common_ancestor(a, 'd', 'h') # b
test_01
lowest_common_ancestor(a, 'd', 'g') # b
test_02
lowest_common_ancestor(a, 'g', 'c') # a
test_03
lowest_common_ancestor(a, 'b', 'g') # b
test_04
lowest_common_ancestor(a, 'f', 'c') # c
example tree
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
test_05
lowest_common_ancestor(l, 'r', 'p') # n
test_06
lowest_common_ancestor(l, 'm', 'o') # l
test_07
lowest_common_ancestor(l, 't', 'q') # n
test_08
lowest_common_ancestor(l, 's', 'p') # p
"""
