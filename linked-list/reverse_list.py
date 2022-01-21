import unittest
from node import Node
from linked_list_values import linked_list_values


def reverse_list(head):
    current = head
    prev = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt

    return prev


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


if __name__ == "__main__":
    unittest.main()
