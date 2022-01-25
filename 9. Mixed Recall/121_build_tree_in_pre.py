"""
build tree in pre
Write a function, build_tree_in_pre, that takes in a list of in-ordered values and a list of pre-ordered values for a binary tree. The function should build a binary tree that has the given in-order and pre-order traversal structure. The function should return the root of this tree.

You can assume that the values of inorder and preorder are unique.

test_00
build_tree_in_pre(
  [ 'z', 'y', 'x' ],
  [ 'y', 'z', 'x' ]
)
#       y
#    /    \
#   z      x
test_01
build_tree_in_pre(
  [ 'y', 'z', 'x' ],
  [ 'y', 'x', 'z' ]
)
#       y
#        \
#         x
#        /
#       z
test_02
build_tree_in_pre(
  [ 'd', 'b', 'g', 'e', 'h', 'a', 'c', 'f' ],
  [ 'a', 'b', 'd', 'e', 'g', 'h', 'c', 'f' ]
)
#       a
#    /    \
#   b      c
#  / \      \
# d   e      f
#    / \
#    g  h
test_03
build_tree_in_pre(
  [ 't', 'u', 's', 'q', 'r', 'p' ],
  [ 'u', 't', 's', 'r', 'q', 'p' ]
)
#     u
#  /    \
# t      s
#         \
#         r
#        / \
#        q  p
test_04
build_tree_in_pre(
  [ 'm', 'l', 'q', 'o', 'r', 'n', 's', 'p', 't' ],
  [ 'l', 'm', 'n', 'o', 'q', 'r', 'p', 's', 't' ]
)
#        l
#     /     \
#    m       n
#         /    \
#         o     p
#        / \   / \
#       q   r s   t
"""
