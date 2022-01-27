"""
--- Insert node ---
Write a function, insert_node, that takes in the head of a linked list, a value, and an index. The function should insert a new node with the value into the list at the specified index. Consider the head of the linked list as index 0. The function should return the head of the resulting linked list.

Do this in-place.

You may assume that the input list is non-empty and the index is not greater than the length of the input list.
"""

import unittest
from node import Node
from _019_linked_list_values import str_list


def insert_node(head, value, index):
    if index == 0:
        node = Node(value)
        node.next = head
        return node

    pos = 0
    current = head
    prev = None
    new_node = Node(value)

    while pos < index:
        pos += 1
        prev = current
        current = current.next
    prev.next = new_node
    new_node.next = current

    return head


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        # a -> b -> c -> d

        result = insert_node(a, 'x', 2)
        assert str_list(result) == "a -> b -> x -> c -> d"

    def test_01(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        # a -> b -> c -> d

        result = insert_node(a, 'v', 3)
        assert str_list(result) == "a -> b -> c -> v -> d"

    def test_02(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        # a -> b -> c -> d

        result = insert_node(a, 'm', 4)
        assert str_list(result) == "a -> b -> c -> d -> m"

    def test_03(self):
        a = Node("a")
        b = Node("b")

        a.next = b

        # a -> b

        result = insert_node(a, 'z', 0)
        assert str_list(result) == "z -> a -> b"


if __name__ == "__main__":
    unittest.main()
