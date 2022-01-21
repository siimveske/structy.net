import unittest
from node import Node


def depth_first_values(root: Node):
    if root is None:
        return []

    values = []
    stack = [root]
    while stack:
        item = stack.pop()
        values.append(item.val)
        if item.right:
            stack.append(item.right)
        if item.left:
            stack.append(item.left)

    return values


def rdepth_first_values(root: Node):
    if root is None:
        return []

    lvalues = rdepth_first_values(root.left)
    rvalues = rdepth_first_values(root.right)

    return [root.val, *lvalues, *rvalues]


class Test(unittest.TestCase):
    def test_00(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        values = depth_first_values(a)
        assert values == ["a", "b", "d", "e", "c", "f"]

    def test_01(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        values = depth_first_values(a)
        assert values == ["a", "b", "d", "e", "g", "c", "f"]

    def test_02(self):
        a = Node("a")
        #     a
        values = depth_first_values(a)
        assert values == ["a"]

    def test_03(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #       \
        #        d
        #         \
        #          e

        values = depth_first_values(a)
        assert values == ["a", "b", "c", "d", "e"]

    def test_04(self):
        values = depth_first_values(None)
        assert values == []

    def test_05(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        values = rdepth_first_values(a)
        assert values == ["a", "b", "d", "e", "c", "f"]

    def test_06(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        values = rdepth_first_values(a)
        assert values == ["a", "b", "d", "e", "g", "c", "f"]

    def test_07(self):
        a = Node("a")
        #     a
        values = rdepth_first_values(a)
        assert values == ["a"]

    def test_08(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #       \
        #        d
        #         \
        #          e

        values = rdepth_first_values(a)
        assert values == ["a", "b", "c", "d", "e"]

    def test_09(self):
        values = rdepth_first_values(None)
        assert values == []


if __name__ == "__main__":
    unittest.main()
