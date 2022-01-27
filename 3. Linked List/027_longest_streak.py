"""
--- Longest streak ---
Write a function, longest_streak, that takes in the head of a linked list as an argument. The function should return the length of the longest consecutive streak of the same value within the list.
"""

import unittest
from node import Node


def longest_streak(head):

    cnt = 0
    longest = 0
    previous = head
    current = head

    while current:
        if current.val == previous.val:
            cnt += 1
            if cnt > longest:
                longest = cnt
        else:
            cnt = 1
        previous = current
        current = current.next

    return longest


class Test(unittest.TestCase):
    def test_00(self):
        a = Node(5)
        b = Node(5)
        c = Node(7)
        d = Node(7)
        e = Node(7)
        f = Node(6)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        # 5 -> 5 -> 7 -> 7 -> 7 -> 6

        assert longest_streak(a) == 3

    def test_01(self):
        a = Node(3)
        b = Node(3)
        c = Node(3)
        d = Node(3)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        # 3 -> 3 -> 3 -> 3 -> 9 -> 9

        assert longest_streak(a) == 4

    def test_02(self):
        a = Node(9)
        b = Node(9)
        c = Node(1)
        d = Node(9)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        # 9 -> 9 -> 1 -> 9 -> 9 -> 9

        assert longest_streak(a) == 3

    def test_03(self):
        a = Node(5)
        b = Node(2)
        c = Node(5)
        d = Node(5)

        a.next = b
        b.next = c
        c.next = d

        # 5 -> 2 -> 5 -> 5

        assert longest_streak(a) == 2

    def test_03(self):
        a = Node(5)
        b = Node(5)

        a.next = b

        # 5 -> 5

        assert longest_streak(a) == 2

    def test_04(self):
        a = Node(4)
        # 4

        assert longest_streak(a) == 1

    def test_05(self):
        assert longest_streak(None) == 0


if __name__ == "__main__":
    unittest.main()
