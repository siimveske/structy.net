import importlib
import unittest
from node import Node

# Hack because python modules can't start with a number
linked = importlib.import_module('019_linked_list_values')
linked_list_values = linked.linked_list_values

"""
--- Reverse list ---
Write a function, reverse_list, that takes in the head of a linked list as an argument. The function should reverse the order of the nodes in the linked list in-place and return the new head of the reversed linked list.
"""


def reverse_list(head):
    """Iterative solution for liked list reversal problem"""
    prev = None
    current = head

    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


def rlist(head, prev=None):
    """Recursive solution for liked list reversal problem"""
    if head is None:
        return prev

    nxt = head.next
    head.next = prev

    return rlist(nxt, head)


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        result = reverse_list(a)
        assert linked_list_values(result) == ["f", "e", "d", "c", "b", "a"]

    def test_01(self):
        x = Node("x")
        y = Node("y")

        x.next = y

        result = reverse_list(x)
        assert linked_list_values(result) == ["y", "x"]

    def test_02(self):
        p = Node("p")
        result = reverse_list(p)
        assert linked_list_values(result) == ["p"]

    def test_03(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        result = rlist(a)
        assert linked_list_values(result) == ["f", "e", "d", "c", "b", "a"]

    def test_04(self):
        x = Node("x")
        y = Node("y")

        x.next = y

        result = rlist(x)
        assert linked_list_values(result) == ["y", "x"]

    def test_05(self):
        p = Node("p")
        result = rlist(p)
        assert linked_list_values(result) == ["p"]


if __name__ == "__main__":
    unittest.main()
