"""
--- Semesters required ---
Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long the prerequisites of a course are satisfied before taking it.

Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.

You can assume that it is possible to eventually complete all courses.
"""


import unittest
from collections import defaultdict


def semesters_required(num_courses, prereqs):
    if not prereqs:
        return 1

    memo = {}
    graph = build_graph(prereqs)
    longest_path = -1
    for node in graph:
        result = explore(graph, node, memo)
        longest_path = max(longest_path, result)

    return longest_path


def build_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
    return graph


def explore(graph, node, memo):
    if node in memo:
        return memo[node]
    if node not in graph:
        memo[node] = 1
        return memo[node]

    longest_path = -1
    for neighbor in graph[node]:
        length = 1 + explore(graph, neighbor, memo)
        longest_path = max(longest_path, length)

    memo[node] = longest_path
    return memo[node]


class Test(unittest.TestCase):
    def test_00(self):
        num_courses = 6
        prereqs = [
            (1, 2),
            (2, 4),
            (3, 5),
            (0, 5),
        ]
        assert semesters_required(num_courses, prereqs) == 3

    def test_01(self):
        num_courses = 7
        prereqs = [
            (4, 3),
            (3, 2),
            (2, 1),
            (1, 0),
            (5, 2),
            (5, 6),
        ]
        assert semesters_required(num_courses, prereqs) == 5

    def test_02(self):
        num_courses = 5
        prereqs = [
            (1, 0),
            (3, 4),
            (1, 2),
            (3, 2),
        ]
        assert semesters_required(num_courses, prereqs) == 2

    def test_03(self):
        num_courses = 12
        prereqs = []
        assert semesters_required(num_courses, prereqs) == 1

    def test_04(self):
        num_courses = 3
        prereqs = [
            (0, 2),
            (0, 1),
            (1, 2),
        ]
        assert semesters_required(num_courses, prereqs) == 3

    def test_05(self):
        num_courses = 6
        prereqs = [
            (3, 4),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 5),
        ]
        assert semesters_required(num_courses, prereqs) == 2


if __name__ == "__main__":
    unittest.main()
