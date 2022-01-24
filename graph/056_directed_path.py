import unittest

"""
--- Has path ---
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
"""


def has_path(graph, src, dst):
    """return a boolean indicating whether or not there
    exists a directed path between the source and destination nodes"""
    stack = [src]
    while stack:
        node = stack.pop()
        if node == dst:
            return True
        stack += graph[node]
    return False


def has_path_rec(graph, src, dst):
    """return a boolean indicating whether or not there
    exists a directed path between the source and destination nodes"""
    if src == dst:
        return True
    for node in graph[src]:
        if has_path_rec(graph, node, dst):
            return True
    return False


class Test(unittest.TestCase):
    def test_01(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        assert has_path(graph, "f", "k") == True

    def test_02(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        assert has_path(graph, "f", "j") == False

    def test_03(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        has_path(graph, "i", "h") == True

    def test_04(self):
        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        assert has_path(graph, "v", "w") == True

    def test_05(self):
        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        assert has_path(graph, "v", "z") == False

    def test_06(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        assert has_path_rec(graph, "f", "k") == True

    def test_07(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        assert has_path_rec(graph, "f", "j") == False

    def test_08(self):
        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        has_path_rec(graph, "i", "h") == True

    def test_09(self):
        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        assert has_path_rec(graph, "v", "w") == True

    def test_10(self):
        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        assert has_path_rec(graph, "v", "z") == False


if __name__ == "__main__":
    unittest.main()
