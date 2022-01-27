"""
--- Remove node ---
Write a function, remove_node, that takes in the head of a linked list and a target value as arguments. The function should delete the node containing the target value from the linked list and return the head of the resulting linked list. If the target appears multiple times in the linked list, only remove the first instance of the target in the list.

Do this in-place.

You may assume that the input list is non-empty.

You may assume that the input list contains the target.
"""
import unittest
from node import Node
from _019_linked_list_values import linked_list_values


def remove_node(head: Node, target_val):
    if head.val == target_val:
        return head.next

    current = head
    previous = None

    while current:
        if current.val == target_val:
            previous.next = current.next
            break
        previous = current
        current = current.next

    return head


def remove_node_rec(head, target_val):
    if not head:
        return None

    if head.val == target_val:
        return head.next

    head.next = remove_node_rec(head.next, target_val)
    return head


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

        # a -> b -> c -> d -> e -> f

        result = remove_node(a, "c")
        assert linked_list_values(result) == ["a", "b", "d", "e", "f"]

    def test_01(self):
        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z

        # x -> y -> z

        result = remove_node(x, "z")
        assert linked_list_values(result) == ["x", "y"]

    def test_02(self):
        q = Node("q")
        r = Node("r")
        s = Node("s")

        q.next = r
        r.next = s

        # q -> r -> s

        result = remove_node(q, "q")
        assert linked_list_values(result) == ["r", "s"]

    def test_03(self):
        node1 = Node("h")
        node2 = Node("i")
        node3 = Node("j")
        node4 = Node("i")

        node1.next = node2
        node2.next = node3
        node3.next = node4

        # h -> i -> j -> i

        result = remove_node(node1, "i")
        assert linked_list_values(result) == ["h", "j", "i"]

    def test_04(self):
        t = Node("t")

        # t

        remove_node(t, "t") == None

    def test_05(self):
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

        result = remove_node_rec(a, "c")
        assert linked_list_values(result) == ["a", "b", "d", "e", "f"]

    def test_06(self):
        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z

        # x -> y -> z

        result = remove_node_rec(x, "z")
        assert linked_list_values(result) == ["x", "y"]

    def test_07(self):
        q = Node("q")
        r = Node("r")
        s = Node("s")

        q.next = r
        r.next = s

        # q -> r -> s

        result = remove_node_rec(q, "q")
        assert linked_list_values(result) == ["r", "s"]

    def test_08(self):
        node1 = Node("h")
        node2 = Node("i")
        node3 = Node("j")
        node4 = Node("i")

        node1.next = node2
        node2.next = node3
        node3.next = node4

        # h -> i -> j -> i

        result = remove_node_rec(node1, "i")
        assert linked_list_values(result) == ["h", "j", "i"]

    def test_09(self):
        t = Node("t")

        # t

        remove_node_rec(t, "t") == None


if __name__ == "__main__":
    unittest.main()
