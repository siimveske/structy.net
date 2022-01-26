"""
--- Is univalue list ---
Write a function, is_univalue_list, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains exactly one unique value.

You may assume that the input list is non-empty.
"""
import unittest
from node import Node


def is_univalue_list(head):
    current = head
    while current:
        if current.val != head.val:
            return False
        current = current.next
    return True


def is_univalue_list_rec(head):
    return _is_univalue_list(head, head.val)


def _is_univalue_list(head, val):
    if not head:
        return True
    if head.val != val:
        return False
    return _is_univalue_list(head.next, val)


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(7)
        b = Node(7)
        c = Node(7)

        a.next = b
        b.next = c

        # 7 -> 7 -> 7

        assert is_univalue_list(a) == True

    def test_01(self):
        a = Node(7)
        b = Node(7)
        c = Node(4)

        a.next = b
        b.next = c

        # 7 -> 7 -> 4

        assert is_univalue_list(a) == False

    def test_02(self):
        u = Node(2)
        v = Node(2)
        w = Node(2)
        x = Node(2)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        # 2 -> 2 -> 2 -> 2 -> 2

        assert is_univalue_list(u) == True

    def test_03(self):
        u = Node(2)
        v = Node(2)
        w = Node(3)
        x = Node(3)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        # 2 -> 2 -> 3 -> 3 -> 2

        assert is_univalue_list(u) == False

    def test_04(self):
        z = Node('z')

        # z

        assert is_univalue_list(z) == True

    def test_05(self):
        a = Node(7)
        b = Node(7)
        c = Node(7)

        a.next = b
        b.next = c

        # 7 -> 7 -> 7

        assert is_univalue_list_rec(a) == True

    def test_06(self):
        a = Node(7)
        b = Node(7)
        c = Node(4)

        a.next = b
        b.next = c

        # 7 -> 7 -> 4

        assert is_univalue_list_rec(a) == False

    def test_07(self):
        u = Node(2)
        v = Node(2)
        w = Node(2)
        x = Node(2)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        # 2 -> 2 -> 2 -> 2 -> 2

        assert is_univalue_list_rec(u) == True

    def test_08(self):
        u = Node(2)
        v = Node(2)
        w = Node(3)
        x = Node(3)
        y = Node(2)

        u.next = v
        v.next = w
        w.next = x
        x.next = y

        # 2 -> 2 -> 3 -> 3 -> 2

        assert is_univalue_list_rec(u) == False

    def test_09(self):
        z = Node('z')

        # z

        assert is_univalue_list_rec(z) == True


if __name__ == "__main__":
    unittest.main()
