"""
--- Safe cracking ---
Oh-no! You forgot the number combination that unlocks your safe. Luckily, you knew that you'd be forgetful so you previously wrote down a bunch of hints that can be used to determine the correct combination. Each hint is a pair of numbers 'x, y' that indicates you must enter digit 'x' before 'y' (but not necessarily immediately before y).

The keypad on the safe has digits 0-9. You can assume that the hints will generate exactly one working combination and that a digit can occur zero or one time in the answer.

Write a function, safe_cracking, that takes in a list of hints as an argument and determines the combination that will unlock the safe. The function should return a string representing the combination.
"""
import unittest


def safe_cracking(hints):
    graph = build_graph(hints)
    num_parents = count_num_of_parents(graph)

    solution = []
    ready = [get_root(num_parents)]

    while ready:
        node = ready.pop()
        solution.append(str(node))

        for child in graph[node]:
            num_parents[child] -= 1
            if num_parents[child] == 0:
                ready.append(child)

    return ''.join(solution)


def get_root(num_parents):
    for parent, count in num_parents.items():
        if count == 0:
            return parent


def count_num_of_parents(graph):
    num_parents = {}

    for node in graph:
        num_parents[node] = 0

    for node in graph:
        for child in graph[node]:
            num_parents[child] += 1

    return num_parents


def build_graph(hints):
    graph = {}
    for node_a, node_b in hints:
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)

    return graph


class Test(unittest.TestCase):
    def test_00(self):
        assert safe_cracking([
            (7, 1),
            (1, 8),
            (7, 8),
        ]) == '718'

    def test_01(self):
        assert safe_cracking([
            (3, 1),
            (4, 7),
            (5, 9),
            (4, 3),
            (7, 3),
            (3, 5),
            (9, 1),
        ]) == '473591'

    def test_02(self):
        assert safe_cracking([
            (2, 5),
            (8, 6),
            (0, 6),
            (6, 2),
            (0, 8),
            (2, 3),
            (3, 5),
            (6, 5),
        ]) == '086235'

    def test_03(self):
        assert safe_cracking([
            (0, 1),
            (6, 0),
            (1, 8),
        ]) == '6018'

    def test_04(self):
        assert safe_cracking([
            (8, 9),
            (4, 2),
            (8, 2),
            (3, 8),
            (2, 9),
            (4, 9),
            (8, 4),
        ]) == '38429'


if __name__ == "__main__":
    unittest.main()
