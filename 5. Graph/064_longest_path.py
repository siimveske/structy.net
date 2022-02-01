"""
--- Longest path ---
Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. The function should return the length of the longest path within the graph. A path may start and end at any two nodes. The length of a path is considered the number of edges in the path, not the number of nodes.
"""
import unittest


def longest_path(graph):
    longest = float("-inf")
    for node in graph:
        stack = [(node, 0)]
        while stack:
            current, distance = stack.pop()
            if not graph[current] and distance > longest:
                longest = distance
                continue
            for neigbor in graph[current]:
                stack.append((neigbor, distance + 1))

    return longest


def longest_path_rec(graph):
    memo = {}
    for node in graph:
        explore(graph, node, memo)
    return max(memo.values())


def explore(graph, node, memo):
    if node in memo:
        return memo[node]

    if not graph[node]:
        memo[node] = 0
        return memo[node]

    best = 0
    for neighbor in graph[node]:
        distance = 1 + explore(graph, neighbor, memo)
        best = max(best, distance)

    memo[node] = best
    return memo[node]


class Test(unittest.TestCase):
    def test_00(self):
        graph = {
            'a': ['c', 'b'],
            'b': ['c'],
            'c': []
        }

        assert longest_path(graph) == 2

    def test_01(self):
        graph = {
            'a': ['c', 'b'],
            'b': ['c'],
            'c': [],
            'q': ['r'],
            'r': ['s', 'u', 't'],
            's': ['t'],
            't': ['u'],
            'u': []
        }

        assert longest_path(graph) == 4

    def test_02(self):
        graph = {
            'h': ['i', 'j', 'k'],
            'g': ['h'],
            'i': [],
            'j': [],
            'k': [],
            'x': ['y'],
            'y': []
        }

        assert longest_path(graph) == 2

    def test_03(self):
        graph = {
            'a': ['b'],
            'b': ['c'],
            'c': [],
            'e': ['f'],
            'f': ['g'],
            'g': ['h'],
            'h': []
        }

        assert longest_path(graph) == 3

    def test_04(self):
        graph = {
            'a': ['c', 'b'],
            'b': ['c'],
            'c': []
        }

        assert longest_path_rec(graph) == 2

    def test_05(self):
        graph = {
            'a': ['c', 'b'],
            'b': ['c'],
            'c': [],
            'q': ['r'],
            'r': ['s', 'u', 't'],
            's': ['t'],
            't': ['u'],
            'u': []
        }

        assert longest_path_rec(graph) == 4

    def test_06(self):
        graph = {
            'h': ['i', 'j', 'k'],
            'g': ['h'],
            'i': [],
            'j': [],
            'k': [],
            'x': ['y'],
            'y': []
        }

        assert longest_path_rec(graph) == 2

    def test_07(self):
        graph = {
            'a': ['b'],
            'b': ['c'],
            'c': [],
            'e': ['f'],
            'f': ['g'],
            'g': ['h'],
            'h': []
        }

        assert longest_path_rec(graph) == 3


if __name__ == "__main__":
    unittest.main()
