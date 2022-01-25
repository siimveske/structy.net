"""
middle value
Write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.

You may assume that the input list is non-empty.

test_00:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')

a.next = b
b.next = c
c.next = d
d.next = e

# a -> b -> c -> d -> e
middle_value(a) # c
test_01:
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# a -> b -> c -> d -> e -> f
middle_value(a) # d
test_02:
x = Node('x')
y = Node('y')
z = Node('z')

x.next = y
y.next = z

# x -> y -> z
middle_value(x) # y
test_03:
x = Node('x')
y = Node('y')

x.next = y

# x -> y
middle_value(x) # y
test_04:
q = Node('q')

# q
middle_value(q) # q
"""
