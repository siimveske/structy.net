import unittest
from node import Node
"""
--- Linked list values ---
Write a function, linked_list_values, that takes in the head of a linked list as an argument. The function should return a list containing all values of the nodes in the linked list.
"""


def linked_list_values(head):
    values = []
    current_node = head

    while current_node:
        values.append(current_node.val)
        current_node = current_node.next

    return values


def str_list(head):
    values = linked_list_values(head)
    result = []
    for idx, value in enumerate(values):
        result.append(str(value))
        if idx < len(values):
            result.append(" -> ")
    return ''.join(result)


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert linked_list_values(a) == ["a", "b", "c", "d"]

    def test_01(self):
        x = Node("x")
        y = Node("y")

        x.next = y

        assert linked_list_values(x) == ["x", "y"]

    def test_02(self):
        x = Node("q")

        assert linked_list_values(x) == ["q"]

    def test_03(self):

        assert linked_list_values(None) == []


if __name__ == "__main__":
    unittest.main()
