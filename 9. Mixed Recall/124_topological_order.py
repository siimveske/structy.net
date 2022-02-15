"""
--- Topological order ---
Write a function, topological_order, that takes in a dictionary representing the adjacency list for a directed-acyclic graph. The function should return a list containing the topological-order of the graph.

The topological ordering of a graph is a sequence where "parent nodes" appear before their "children" within the sequence.
"""
import unittest


def topological_order(graph):
    num_parents = {}
    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    ready = []
    for parent, count in num_parents.items():
        if count == 0:
            ready.append(parent)
            break

    solution = []
    while ready:
        current_item = ready.pop()
        solution.append(current_item)

        for child in graph[current_item]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return solution


class Test(unittest.TestCase):
    def test_00(self):
        assert topological_order({
            "a": ["f"],
            "b": ["d"],
            "c": ["a", "f"],
            "d": ["e"],
            "e": [],
            "f": ["b", "e"],
        }) == ['c', 'a', 'f', 'b', 'd', 'e']

    def test_01(self):
        assert topological_order({
            "h": ["l", "m"],
            "i": ["k"],
            "j": ["k", "i"],
            "k": ["h", "m"],
            "l": ["m"],
            "m": [],
        }) == ['j', 'i', 'k', 'h', 'l', 'm']

    def test_02(self):
        assert topological_order({
            "q": [],
            "r": ["q"],
            "s": ["r"],
            "t": ["s"],
        }) == ['t', 's', 'r', 'q']

    def test_03(self):
        assert topological_order({
            "v": ["z", "w"],
            "w": [],
            "x": ["w", "v", "z"],
            "y": ["x"],
            "z": ["w"],
        }) == ['y', 'x', 'v', 'z', 'w']


if __name__ == "__main__":
    unittest.main()
