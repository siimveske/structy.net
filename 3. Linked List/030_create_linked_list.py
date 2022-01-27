"""
--- Create linked list ---
Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.
"""
import unittest
from node import Node
from _019_linked_list_values import str_list


def create_linked_list(values):
    root = Node(None)
    current = root
    for value in values:
        current.next = Node(value)
        current = current.next

    return root.next


def create_linked_list_rec(values):
    return _create_linked_list(values, 0)


def _create_linked_list(values, idx):
    if idx >= len(values):
        return None

    node = Node(values[idx])
    node.next = _create_linked_list(values, idx + 1)
    return node


class Test(unittest.TestCase):
    def test_00(self):
        result = create_linked_list(["h", "e", "y"])
        assert str_list(result) == "h -> e -> y"

    def test_01(self):
        result = create_linked_list([1, 7, 1, 8])
        assert str_list(result) == "1 -> 7 -> 1 -> 8"

    def test_02(self):
        result = create_linked_list(["a"])
        assert str_list(result) == "a"

    def test_03(self):
        assert create_linked_list([]) == None

    def test_04(self):
        result = create_linked_list_rec(["h", "e", "y"])
        assert str_list(result) == "h -> e -> y"

    def test_05(self):
        result = create_linked_list_rec([1, 7, 1, 8])
        assert str_list(result) == "1 -> 7 -> 1 -> 8"

    def test_06(self):
        result = create_linked_list_rec(["a"])
        assert str_list(result) == "a"

    def test_07(self):
        assert create_linked_list_rec([]) == None


if __name__ == "__main__":
    unittest.main()
