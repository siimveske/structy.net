"""
--- Tolerant teams ---
Write a function, tolerant_teams, that takes in a list of rivalries as an argument. A rivalry is a pair of people who should not be placed on the same team. The function should return a boolean indicating whether or not it is possible to separate people into two teams, without rivals being on the same team. The two teams formed do not have to be the same size.
"""
import unittest
from collections import defaultdict


def tolerant_teams(rivalries):
    colors = {}
    graph = build_graph(rivalries)
    for node in graph:
        if node in colors:
            continue
        if explore(graph, node, colors, True) == False:
            return False
    return True


def explore(graph, node, colors, color):
    if node in colors:
        return colors[node] == color

    colors[node] = color

    for neighbor in graph[node]:
        if explore(graph, neighbor, colors, not color) == False:
            return False

    return True


def build_graph(rivalries):
    result = defaultdict(list)
    for r1, r2 in rivalries:
        result[r1].append(r2)
        result[r2].append(r1)
    return result


class Test(unittest.TestCase):
    def test_00(self):
        assert tolerant_teams([
            ('philip', 'seb'),
            ('raj', 'nader')
        ]) == True

    def test_01(self):
        assert tolerant_teams([
            ('philip', 'seb'),
            ('raj', 'nader'),
            ('raj', 'philip'),
            ('seb', 'raj')
        ]) == False

    def test_02(self):
        assert tolerant_teams([
            ('cindy', 'anj'),
            ('alex', 'matt'),
            ('alex', 'cindy'),
            ('anj', 'matt'),
            ('brando', 'matt')
        ]) == True

    def test_03(self):
        assert tolerant_teams([
            ('alex', 'anj'),
            ('alex', 'matt'),
            ('alex', 'cindy'),
            ('anj', 'matt'),
            ('brando', 'matt')
        ]) == False

    def test_04(self):
        assert tolerant_teams([
            ('alan', 'jj'),
            ('betty', 'richard'),
            ('jj', 'simcha'),
            ('richard', 'christine')
        ]) == True

    def test_05(self):
        assert tolerant_teams([
            ('alan', 'jj'),
            ('betty', 'richard'),
            ('jj', 'simcha'),
            ('richard', 'christine')
        ]) == True

    def test_06(self):
        assert tolerant_teams([
            ('alan', 'jj'),
            ('jj', 'richard'),
            ('betty', 'richard'),
            ('jj', 'simcha'),
            ('richard', 'christine')
        ]) == True

    def test_07(self):
        assert tolerant_teams([
            ('alan', 'jj'),
            ('betty', 'richard'),
            ('betty', 'christine'),
            ('jj', 'simcha'),
            ('richard', 'christine')
        ]) == False


if __name__ == "__main__":
    unittest.main()
