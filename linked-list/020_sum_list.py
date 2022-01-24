import unittest
from node import Node

"""
--- sum list ---
Write a function, sum_list, that takes in the head of a linked list containing numbers as an argument. The function should return the total sum of all values in the linked list.
"""


def sum_list(head):
    total = 0
    current_node = head

    while current_node:
        total += current_node.val
        current_node = current_node.next

    return total


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(2)
        b = Node(8)
        c = Node(3)
        d = Node(-1)
        e = Node(7)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        assert sum_list(a) == 19

    def test_01(self):
        x = Node(38)
        y = Node(4)

        x.next = y

        assert sum_list(x) == 42

    def test_02(self):
        z = Node(100)
        assert sum_list(z) == 100

    def test_03(self):
        assert sum_list(None) == 0


if __name__ == "__main__":
    unittest.main()
