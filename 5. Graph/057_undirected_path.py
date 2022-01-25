import unittest
from collections import defaultdict

"""
--- Undirected path ---
Write a function, undirected_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return a boolean indicating whether or not there exists a path between node_A and node_B.
"""


def undirected_path(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path(graph, node_A, node_B)


def undirected_path_rec(edges, node_A, node_B):
    graph = build_graph(edges)
    return has_path_rec(graph, node_A, node_B, set())


def build_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


def has_path(graph, start, end):
    """The function returns a boolean indicating whether
    or not there exists a path between node_A and node_B"""

    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        if node == end:
            return True
        visited.add(node)
        stack += graph[node]

    return False


def has_path_rec(graph, start, end, visited):
    """The function returns a boolean indicating whether
    or not there exists a path between node_A and node_B"""

    if start == end:
        return True

    visited.add(start)

    for node in graph[start]:
        if node in visited:
            continue
        if has_path_rec(graph, node, end, visited):
            return True

    return False


class Test(unittest.TestCase):
    def test_01(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path(edges, 'j', 'm') == True

    def test_02(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path(edges, 'm', 'j') == True

    def test_03(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path(edges, 'l', 'j') == True

    def test_04(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path(edges, 'k', 'o') == False

    def test_05(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path(edges, 'i', 'o') == False

    def test_06(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path(edges, 'a', 'b') == True

    def test_07(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path(edges, 'a', 'c') == True

    def test_08(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path(edges, 'r', 't') == True

    def test_09(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path(edges, 'r', 'b') == False

    def test_10(self):
        edges = [
            ('s', 'r'),
            ('t', 'q'),
            ('q', 'r'),
        ]

        undirected_path(edges, 'r', 't') == True

    def test_11(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path_rec(edges, 'j', 'm') == True

    def test_12(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path_rec(edges, 'm', 'j') == True

    def test_13(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path_rec(edges, 'l', 'j') == True

    def test_14(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path_rec(edges, 'k', 'o') == False

    def test_15(self):
        edges = [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

        assert undirected_path_rec(edges, 'i', 'o') == False

    def test_16(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path_rec(edges, 'a', 'b') == True

    def test_17(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path_rec(edges, 'a', 'c') == True

    def test_18(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path_rec(edges, 'r', 't') == True

    def test_19(self):
        edges = [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

        undirected_path_rec(edges, 'r', 'b') == False

    def test_20(self):
        edges = [
            ('s', 'r'),
            ('t', 'q'),
            ('q', 'r'),
        ]

        undirected_path_rec(edges, 'r', 't') == True


if __name__ == '__main__':
    unittest.main()
