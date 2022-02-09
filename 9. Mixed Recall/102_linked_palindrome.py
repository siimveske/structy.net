"""
--- Linked palindrome ---
Write a function, linked_palindrome, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list is a palindrome. A palindrome is a sequence that is the same both forwards and backwards.
"""
import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_palindrome(head: Node):
    values = []

    current = head
    while current:
        values.append(current.val)
        current = current.next

    reversed = values[::-1]
    return values == reversed


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(3)
        b = Node(2)
        c = Node(7)
        d = Node(7)
        e = Node(2)
        f = Node(3)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        # 3 -> 2 -> 7 -> 7 -> 2 -> 3
        assert linked_palindrome(a) == True

    def test_01(self):
        a = Node(3)
        b = Node(2)
        c = Node(4)

        a.next = b
        b.next = c

        # 3 -> 2 -> 4
        assert linked_palindrome(a) == False

    def test_02(self):
        a = Node(3)
        b = Node(2)
        c = Node(3)

        a.next = b
        b.next = c

        # 3 -> 2 -> 3
        assert linked_palindrome(a) == True

    def test_03(self):
        a = Node(0)
        b = Node(1)
        c = Node(0)
        d = Node(1)
        e = Node(0)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        # 0 -> 1 -> 0 -> 1 -> 0
        assert linked_palindrome(a) == True

    def test_04(self):
        a = Node(0)
        b = Node(1)
        c = Node(0)
        d = Node(1)
        e = Node(1)

        a.next = b
        b.next = c
        c.next = d
        d.next = e

        # 0 -> 1 -> 0 -> 1 -> 1
        assert linked_palindrome(a) == False

    def test_05(self):
        a = Node(5)

        # 5
        assert linked_palindrome(a) == True

    def test_06(self):
        assert linked_palindrome(None) == True


if __name__ == "__main__":
    unittest.main()
