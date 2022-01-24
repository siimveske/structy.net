import unittest
from node import Node

"""
--- Get node value ---
Write a function, get_node_value, that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.

If there is no node at the given index, then return None.
"""


def get_node_value(head, index):
    if head is None:
        return None

    position = 0
    current_node = head
    while position < index:
        if current_node.next is None:
            return None
        current_node = current_node.next
        position += 1

    return current_node.val


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert get_node_value(a, 2) == "c"

    def test_01(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert get_node_value(a, 3) == "d"

    def test_02(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert get_node_value(a, 7) == None

    def test_03(self):
        node1 = Node("banana")
        node2 = Node("mango")

        node1.next = node2

        assert get_node_value(node1, 0) == "banana"

    def test_04(self):
        node1 = Node("banana")
        node2 = Node("mango")

        node1.next = node2

        assert get_node_value(node1, 1) == "mango"


if __name__ == "__main__":
    unittest.main()
