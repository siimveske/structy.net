import unittest
from node import Node


def linked_list_find(head, target):
    current_node = head

    while current_node:
        if current_node.val == target:
            return True
        current_node = current_node.next

    return False


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert linked_list_find(a, "c") == True

    def test_01(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert linked_list_find(a, "d") == True

    def test_02(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        assert linked_list_find(a, "q") == False

    def test_03(self):
        node1 = Node("jason")
        node2 = Node("leneli")

        node1.next = node2

        assert linked_list_find(node1, "jason") == True

    def test_04(self):
        node1 = Node(42)
        assert linked_list_find(node1, 42) == True

    def test_05(self):
        node1 = Node(42)
        assert linked_list_find(node1, 100) == False


if __name__ == "__main__":
    unittest.main()
