import unittest
from node import Node


def linked_list_values(head):
    values = []
    current_node = head

    while current_node:
        values.append(current_node.val)
        current_node = current_node.next

    return values


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
