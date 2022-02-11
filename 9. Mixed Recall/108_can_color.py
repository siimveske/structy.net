"""
--- Can color ---
Write a function, can_color, that takes in a dictionary representing the adjacency list of an undirected graph. The function should return a boolean indicating whether or not it is possible to color nodes of the graph using two colors in such a way that adjacent nodes are always different colors.

For example, given this graph:

x-y-z

It is possible to color the nodes by using red for x and z,
then use blue for y. So the answer is True.

For example, given this graph:

    q
   / \
  s - r

It is not possible to color the nodes without making two
adjacent nodes the same color. So the answer is False.
"""
import unittest


def can_color(graph):
    colors = {}
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


class Test(unittest.TestCase):
    def test_00(self):
        assert can_color({
            "x": ["y"],
            "y": ["x", "z"],
            "z": ["y"]
        }) == True

    def test_01(self):
        assert can_color({
            "q": ["r", "s"],
            "r": ["q", "s"],
            "s": ["r", "q"]
        }) == False

    def test_02(self):
        assert can_color({
            "a": ["b", "c", "d"],
            "b": ["a"],
            "c": ["a"],
            "d": ["a"],
        }) == True

    def test_03(self):
        assert can_color({
            "a": ["b", "c", "d"],
            "b": ["a"],
            "c": ["a", "d"],
            "d": ["a", "c"],
        }) == False

    def test_04(self):
        assert can_color({
            "h": ["i", "k"],
            "i": ["h", "j"],
            "j": ["i", "k"],
            "k": ["h", "j"],
        }) == True

    def test_05(self):
        assert can_color({
            "z": []
        }) == True

    def test_06(self):
        assert can_color({
            "h": ["i", "k"],
            "i": ["h", "j"],
            "j": ["i", "k"],
            "k": ["h", "j"],
            "q": ["r", "s"],
            "r": ["q", "s"],
            "s": ["r", "q"]
        }) == False


if __name__ == "__main__":
    unittest.main()
