"""
--- Middle value ---
Write a function, middle_value, that takes in the head of a linked list as an argument. The function should return the value of the middle node in the linked list. If the linked list has an even number of nodes, then return the value of the second middle node.

You may assume that the input list is non-empty.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def middle_value(head: Node):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    return slow.val


class Test(unittest.TestCase):
    def test_00(self):
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
        assert middle_value(a) == 'c'

    def test_01(self):
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
        assert middle_value(a) == 'd'

    def test_02(self):
        x = Node('x')
        y = Node('y')
        z = Node('z')

        x.next = y
        y.next = z

        # x -> y -> z
        assert middle_value(x) == 'y'

    def test_03(self):
        x = Node('x')
        y = Node('y')

        x.next = y

        # x -> y
        assert middle_value(x) == 'y'

    def test_04(self):
        q = Node('q')

        # q
        assert middle_value(q) == 'q'


if __name__ == "__main__":
    unittest.main()
