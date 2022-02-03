"""
--- Prereqs possible ---
Write a function, prereqs_possible, that takes in a number of courses (n) and prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. The function should return a boolean indicating whether or not it is possible to complete all courses.
"""


import unittest


def prereqs_possible(num_courses: int, prereqs: tuple) -> bool:
    graph = build_graph(num_courses, prereqs)
    for node in graph:
        if _has_loop(graph, node, set(), set()):
            return False
    return True


def _has_loop(graph: dict, node: int, gray: set, black: set) -> bool:
    if node in gray:
        return True
    if node in black:
        return False

    gray.add(node)

    for neighbor in graph[node]:
        if _has_loop(graph, neighbor, gray, black):
            return True

    gray.remove(node)
    black.add(node)

    return False


def build_graph(num_courses: int, prereqs: tuple) -> dict:
    graph = {}
    for i in range(num_courses):
        graph[i] = []
    for key, val in prereqs:
        graph[key].append(val)
    return graph


class Test(unittest.TestCase):
    def test_00(self):
        numCourses = 6
        prereqs = [
            (0, 1),
            (2, 3),
            (0, 2),
            (1, 3),
            (4, 5),
        ]
        assert prereqs_possible(numCourses, prereqs) == True

    def test_01(self):
        numCourses = 6
        prereqs = [
            (0, 1),
            (2, 3),
            (0, 2),
            (1, 3),
            (4, 5),
            (3, 0),
        ]
        assert prereqs_possible(numCourses, prereqs) == False

    def test_02(self):
        numCourses = 5
        prereqs = [
            (2, 4),
            (1, 0),
            (0, 2),
            (0, 4),
        ]
        assert prereqs_possible(numCourses, prereqs) == True

    def test_03(self):
        numCourses = 6
        prereqs = [
            (2, 4),
            (1, 0),
            (0, 2),
            (0, 4),
            (5, 3),
            (3, 5),
        ]
        assert prereqs_possible(numCourses, prereqs) == False

    def test_04(self):
        numCourses = 8
        prereqs = [
            (1, 0),
            (0, 6),
            (2, 0),
            (0, 5),
            (3, 7),
            (4, 3),
        ]
        assert prereqs_possible(numCourses, prereqs) == True

    def test_05(self):
        numCourses = 8
        prereqs = [
            (1, 0),
            (0, 6),
            (2, 0),
            (0, 5),
            (3, 7),
            (7, 4),
            (4, 3),
        ]
        assert prereqs_possible(numCourses, prereqs) == False

    def test_06(self):
        numCourses = 42
        prereqs = [(6, 36)]
        assert prereqs_possible(numCourses, prereqs) == True


if __name__ == "__main__":
    unittest.main()
