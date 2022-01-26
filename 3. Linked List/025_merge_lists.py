"""
--- Merge lists ---
Write a function, merge_lists, that takes in the head of two sorted linked lists as arguments. The function should merge the two lists together into single sorted linked list. The function should return the head of the merged linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty and contain increasing sorted numbers.
"""
import unittest
from node import Node
from _019_linked_list_values import linked_list_values


def merge_lists(head_1, head_2):
    pass  # todo


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(5)
        b = Node(7)
        c = Node(10)
        d = Node(12)
        e = Node(20)
        f = Node(28)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # 5 -> 7 -> 10 -> 12 -> 20 -> 28

        q = Node(6)
        r = Node(8)
        s = Node(9)
        t = Node(25)
        q.next = r
        r.next = s
        s.next = t
        # 6 -> 8 -> 9 -> 25

        result = merge_lists(a, q)
        values = linked_list_values(result)
        assert values == [5, 6, 7, 8, 9, 10, 12, 20, 25, 28]

    def test_01(self):
        a = Node(5)
        b = Node(7)
        c = Node(10)
        d = Node(12)
        e = Node(20)
        f = Node(28)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # 5 -> 7 -> 10 -> 12 -> 20 -> 28

        q = Node(1)
        r = Node(8)
        s = Node(9)
        t = Node(10)
        q.next = r
        r.next = s
        s.next = t
        # 1 -> 8 -> 9 -> 10

        result = merge_lists(a, q)
        values = linked_list_values(result)
        assert values == [1, 5, 7, 8, 9, 10, 10, 12, 20, 28]

    def test_02(self):
        h = Node(30)
        # 30

        p = Node(15)
        q = Node(67)
        p.next = q
        # 15 -> 67

        result = merge_lists(h, p)
        values = linked_list_values(result)
        assert values == [15, 30, 67]


if __name__ == "__main__":
    unittest.main()
