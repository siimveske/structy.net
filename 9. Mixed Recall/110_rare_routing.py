"""
--- Rare routing ---
Write a function, rare_routing, that takes in a number of cities (n) and a list of tuples where each tuple represents a direct road that connects a pair of cities. The function should return a boolean indicating whether or not there exists a unique route for every pair of cities. A route is a sequence of roads that does not visit a city more than once.

Cities will be numbered 0 to n - 1.

You can assume that all roads are two-way roads. This means if there is a road between A and B, then you can use that road to go from A to B or go from B to A.

For example, given these roads:

0 --- 1
| \
|  \
|   \
2    3

There is a unique route for between every pair of cities.
So the answer is True.


For example, given these roads:

0 --- 1
| \
|  \
|   \
2 -- 3

There are two routes that can be used to travel from city 1 to city 2:
- first route:  1, 0, 2
- second route: 1, 0, 3, 2
The answer is False, because routes should be unique.
"""
import unittest


def rare_routing(n, roads):
    graph = build_graph(n, roads)

    visited = set()
    if explore(0, graph, visited, previous=None) == False:
        return False

    for node in graph:
        if node not in visited:
            return False

    return True


def explore(node, graph, visited, previous):
    if node in visited:
        return False

    visited.add(node)

    for neigbour in graph[node]:
        if neigbour != previous:
            if explore(neigbour, graph, visited, node) == False:
                return False

    return True


def build_graph(n, roads):
    result = {}
    for i in range(n):
        result[i] = []

    for r1, r2 in roads:
        result[r1].append(r2)
        result[r2].append(r1)
    return result


class Test(unittest.TestCase):
    def test_00(self):
        assert rare_routing(4, [
            (0, 1),
            (0, 2),
            (0, 3)
        ]) == True

    def test_01(self):
        assert rare_routing(4, [
            (0, 1),
            (0, 2),
            (0, 3),
            (3, 2)
        ]) == False

    def test_02(self):
        assert rare_routing(6, [
            (1, 2),
            (5, 4),
            (3, 0),
            (0, 1),
            (0, 4),
        ]) == True

    def test_03(self):
        assert rare_routing(6, [
            (1, 2),
            (4, 1),
            (5, 4),
            (3, 0),
            (0, 1),
            (0, 4),
        ]) == False

    def test_04(self):
        assert rare_routing(4, [
            (0, 1),
            (3, 2),
        ]) == False


if __name__ == "__main__":
    unittest.main()
