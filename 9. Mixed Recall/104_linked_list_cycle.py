"""
--- Linked list cycle ---
Write a function, linked_list_cycle, that takes in the head of a linked list as an argument. The function should return a boolean indicating whether or not the linked list contains a cycle.
"""
import unittest


def linked_list_cycle(head):
    visited = set()
    current = head

    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next

    return False


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Test(unittest.TestCase):
    def test_00(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.next = b
        b.next = c
        c.next = d
        d.next = b  # cycle

        #         _______
        #       /        \
        # a -> b -> c -> d

        assert linked_list_cycle(a) == True

    def test_01(self):
        q = Node('q')
        r = Node('r')
        s = Node('s')
        t = Node('t')
        u = Node('u')

        q.next = r
        r.next = s
        s.next = t
        t.next = u
        u.next = q  # cycle

        #    ________________
        #  /                 \
        # q -> r -> s -> t -> u

        assert linked_list_cycle(q) == True

    def test_02(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')

        a.next = b
        b.next = c
        c.next = d

        # a -> b -> c -> d

        assert linked_list_cycle(a) == False

    def test_03(self):
        q = Node('q')
        r = Node('r')
        s = Node('s')
        t = Node('t')
        u = Node('u')

        q.next = r
        r.next = s
        s.next = t
        t.next = u
        u.next = t  # cycle

        #                   __
        #                 /   \
        # q -> r -> s -> t -> u

        assert linked_list_cycle(q) == True

    def test_04(self):
        p = Node('p')
        # p
        assert linked_list_cycle(p) == False

    def test_05(self):
        assert linked_list_cycle(None) == False


if __name__ == "__main__":
    unittest.main()
