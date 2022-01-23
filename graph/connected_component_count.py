import unittest


def connected_components_count(graph):
    """Return the number of connected components within the graph"""

    visited = set()
    count = 0

    for start in graph:
        if start in visited:
            continue
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack += graph[node]
        count += 1

    return count


def connected_components_count_rec(graph):
    """Return the number of connected components within the graph"""

    visited = set()
    count = 0

    for node in graph:
        if node in visited:
            continue
        explore(graph, node, visited)
        count += 1

    return count


def explore(graph, src, visited):
    visited.add(src)
    for node in graph[src]:
        if node in visited:
            continue
        explore(graph, node, visited)


class Test(unittest.TestCase):
    def test_00(self):
        assert connected_components_count({
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }) == 2

    def test_01(self):
        assert connected_components_count({
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }) == 1

    def test_02(self):
        assert connected_components_count({
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        }) == 3

    def test_03(self):
        assert connected_components_count({}) == 0

    def test_04(self):
        assert connected_components_count({
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }) == 5

    def test_05(self):
        assert connected_components_count_rec({
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }) == 2

    def test_06(self):
        assert connected_components_count_rec({
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }) == 1

    def test_07(self):
        assert connected_components_count_rec({
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        }) == 3

    def test_08(self):
        assert connected_components_count_rec({}) == 0

    def test_09(self):
        assert connected_components_count_rec({
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }) == 5


if __name__ == '__main__':
    unittest.main()
