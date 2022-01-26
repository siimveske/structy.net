import importlib
import unittest
from node import Node
from _019_linked_list_values import linked_list_values
"""
--- Zipper lists ---
Write a function, zipper_lists, that takes in the head of two linked lists as arguments. The function should zipper the two lists together into single linked list by alternating nodes. If one of the linked lists is longer than the other, the resulting list should terminate with the remaining nodes. The function should return the head of the zippered linked list.

Do this in-place, by mutating the original Nodes.

You may assume that both input lists are non-empty.
"""


def zipper_lists(head_1: Node, head_2: Node):
    """Iterative solution for list zipping"""
    count = 0
    tail = head_1
    current1 = head_1.next
    current2 = head_2

    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        count += 1
        tail = tail.next

    if current1:
        tail.next = current1
    elif current2:
        tail.next = current2

    return head_1


def rzipper_lists(head_1: Node, head_2: Node):
    """Recursive solution for list zipping"""
    if head_1 is None and head_2 is None:
        return None
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1
    next1 = head_1.next
    next2 = head_2.next
    head_1.next = head_2
    head_2.next = rzipper_lists(next1, next2)
    return head_1


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.next = b
        b.next = c
        # a -> b -> c

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z
        # x -> y -> z

        result = zipper_lists(a, x)
        # a -> x -> b -> y -> c -> z
        values = linked_list_values(result)
        assert values == ["a", "x", "b", "y", "c", "z"]

    def test_01(self):
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
        # a -> b -> c -> d -> e -> f

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z
        # x -> y -> z

        result = zipper_lists(a, x)
        # a -> x -> b -> y -> c -> z -> d -> e -> f
        values = linked_list_values(result)
        assert values == ["a", "x", "b", "y", "c", "z", "d", "e", "f"]

    def test_02(self):
        s = Node("s")
        t = Node("t")
        s.next = t
        # s -> t

        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        one.next = two
        two.next = three
        three.next = four
        # 1 -> 2 -> 3 -> 4

        result = zipper_lists(s, one)
        # s -> 1 -> t -> 2 -> 3 -> 4

        values = linked_list_values(result)
        assert values == ["s", 1, "t", 2, 3, 4]

    def test_03(self):
        w = Node("w")
        # w

        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three
        # 1 -> 2 -> 3

        result = zipper_lists(w, one)
        # w -> 1 -> 2 -> 3

        values = linked_list_values(result)
        assert values == ["w", 1, 2, 3]

    def test_04(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three
        # 1 -> 2 -> 3

        w = Node("w")
        # w

        result = zipper_lists(one, w)
        # 1 -> w -> 2 -> 3

        values = linked_list_values(result)
        assert values == [1, "w", 2, 3]

    def test_05(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        a.next = b
        b.next = c
        # a -> b -> c

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z
        # x -> y -> z

        result = rzipper_lists(a, x)
        # a -> x -> b -> y -> c -> z
        values = linked_list_values(result)
        assert values == ["a", "x", "b", "y", "c", "z"]

    def test_06(self):
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
        # a -> b -> c -> d -> e -> f

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z
        # x -> y -> z

        result = rzipper_lists(a, x)
        # a -> x -> b -> y -> c -> z -> d -> e -> f
        values = linked_list_values(result)
        assert values == ["a", "x", "b", "y", "c", "z", "d", "e", "f"]

    def test_07(self):
        s = Node("s")
        t = Node("t")
        s.next = t
        # s -> t

        one = Node(1)
        two = Node(2)
        three = Node(3)
        four = Node(4)
        one.next = two
        two.next = three
        three.next = four
        # 1 -> 2 -> 3 -> 4

        result = rzipper_lists(s, one)
        # s -> 1 -> t -> 2 -> 3 -> 4

        values = linked_list_values(result)
        assert values == ["s", 1, "t", 2, 3, 4]

    def test_08(self):
        w = Node("w")
        # w

        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three
        # 1 -> 2 -> 3

        result = rzipper_lists(w, one)
        # w -> 1 -> 2 -> 3

        values = linked_list_values(result)
        assert values == ["w", 1, 2, 3]

    def test_09(self):
        one = Node(1)
        two = Node(2)
        three = Node(3)
        one.next = two
        two.next = three
        # 1 -> 2 -> 3

        w = Node("w")
        # w

        result = rzipper_lists(one, w)
        # 1 -> w -> 2 -> 3

        values = linked_list_values(result)
        assert values == [1, "w", 2, 3]


if __name__ == "__main__":
    unittest.main()
