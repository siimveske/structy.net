from collections import deque
from collections import defaultdict
import unittest

"""
--- Shortest path ---
Write a function, shortest_path, that takes in a list of edges for an undirected graph and two nodes (node_A, node_B). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B, then return -1.
"""


def build_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


def shortest_path(edges, node_A, node_B):
    graph = build_graph(edges)

    visited = set(node_A)
    queue = deque([(node_A, 0)])

    while queue:
        node, distance = queue.popleft()
        if node == node_B:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1


class Test(unittest.TestCase):
    def test_00(self):
        edges = [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]
        assert shortest_path(edges, 'w', 'z') == 2

    def test_01(self):
        edges = [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]
        assert shortest_path(edges, 'y', 'x') == 1

    def test_02(self):
        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]
        assert shortest_path(edges, 'a', 'e') == 3

    def test_03(self):
        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]
        assert shortest_path(edges, 'e', 'c') == 2

    def test_04(self):
        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]
        assert shortest_path(edges, 'b', 'g') == -1

    def test_05(self):
        edges = [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]
        assert shortest_path(edges, 'w', 'e') == 1

    def test_06(self):
        edges = [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]
        assert shortest_path(edges, 'n', 'e') == 2

    def test_07(self):
        edges = [
            ['m', 'n'],
            ['n', 'o'],
            ['o', 'p'],
            ['p', 'q'],
            ['t', 'o'],
            ['r', 'q'],
            ['r', 's']
        ]
        assert shortest_path(edges, 'm', 's') == 6


if __name__ == '__main__':
    unittest.main()
