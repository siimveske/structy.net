import unittest
from node import Node


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

        assert reverse_list(a).val == 'f'

    def test_01(self):
        x = Node("x")
        y = Node("y")

        x.next = y

        assert reverse_list(x).val == 'y'

    def test_02(self):
        p = Node("p")
        assert reverse_list(p).val == 'p'


if __name__ == "__main__":
    unittest.main()
