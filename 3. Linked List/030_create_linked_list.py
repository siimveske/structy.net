"""
--- Create linked list ---
Write a function, create_linked_list, that takes in a list of values as an argument. The function should create a linked list containing each item of the list as the values of the nodes. The function should return the head of the linked list.
"""
import unittest
from node import Node
from _019_linked_list_values import str_list


def create_linked_list(values):
    if not values:
        return None

    root = Node(None)
    current = root
    for value in values:
        current.next = Node(value)
        current = current.next

    return root.next


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


if __name__ == "__main__":
    unittest.main()
