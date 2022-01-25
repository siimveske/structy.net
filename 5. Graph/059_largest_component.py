import unittest
"""
--- Largest component ---
Write a function, largest_component, that takes in the adjacency list of an undirected graph. The function should return the size of the largest connected component in the graph.
"""


def largest_component(graph):
    """Find the size of the largest connected
    component (island of nodes)in the graph"""

    result = 0
    visited = set()

    for start in graph:
        if start in visited:
            continue

        stack = [start]
        component = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            stack += graph[node]

        if len(component) > result:
            result = len(component)

    return result


def largest_component_rec(graph):
    """Find the size of the largest connected
    component (island of nodes)in the graph"""

    result = 0
    visited = set()

    for node in graph:
        if node in visited:
            continue
        count = explore(graph, node, visited)
        if count > result:
            result = count

    return result


def explore(graph, src, visited):

    size = 1
    visited.add(src)

    for node in graph[src]:
        if node in visited:
            continue
        size += explore(graph, node, visited)

    return size


class Test(unittest.TestCase):
    def test_00(self):
        assert largest_component({
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }) == 4

    def test_01(self):
        assert largest_component({
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }) == 6

    def test_02(self):
        assert largest_component({
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        }) == 5

    def test_03(self):
        assert largest_component({}) == 0

    def test_04(self):
        assert largest_component({
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }) == 3

    def test_05(self):
        assert largest_component_rec({
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }) == 4

    def test_06(self):
        assert largest_component_rec({
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }) == 6

    def test_07(self):
        assert largest_component_rec({
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        }) == 5

    def test_08(self):
        assert largest_component_rec({}) == 0

    def test_09(self):
        assert largest_component_rec({
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }) == 3


if __name__ == '__main__':
    unittest.main()
