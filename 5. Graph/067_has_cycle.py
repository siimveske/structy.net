"""
--- Has cycle ---
Write a function, has_cycle, that takes in an object representing the adjacency list of a directed graph. The function should return a boolean indicating whether or not the graph contains a cycle.
"""


import unittest


# def has_cycle(graph):
#     visited = set()
#     for node in graph:
#         stack = [node]
#         visiting = set()
#         while stack:
#             current = stack.pop()

#             if current in visiting:
#                 return True
#             if current in visited:
#                 continue

#             visiting.add(current)

#             if not graph[current]:
#                 visited = visited.union(visiting)
#                 visiting = set()

#             for neighbor in graph[current]:
#                 stack.append(neighbor)

#         visited = visited.union(visiting)
#     return False

def has_cycle(graph):
    visited = set()
    for start_node in graph:
        if cycle_detect(graph, start_node, set(), visited):
            return True
    return False


def cycle_detect(graph, node, visiting, visited):
    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited):
            return True

    visiting.remove(node)
    visited.add(node)
    return False


class Test(unittest.TestCase):
    def test_00(self):
        assert has_cycle({
            "a": ["b"],
            "b": ["c"],
            "c": ["a"],
        }) == True

    def test_01(self):
        assert has_cycle({
            "a": ["b", "c"],
            "b": ["c"],
            "c": ["d"],
            "d": [],
        }) == False

    def test_02(self):
        assert has_cycle({
            "a": ["b", "c"],
            "b": [],
            "c": [],
            "e": ["f"],
            "f": ["e"],
        }) == True

    def test_03(self):
        assert has_cycle({
            "q": ["r", "s"],
            "r": ["t", "u"],
            "s": [],
            "t": [],
            "u": [],
            "v": ["w"],
            "w": [],
            "x": ["w"],
        }) == False

    def test_04(self):
        assert has_cycle({
            "a": ["b"],
            "b": ["c"],
            "c": ["a"],
            "g": [],
        }) == True


if __name__ == "__main__":
    unittest.main()
