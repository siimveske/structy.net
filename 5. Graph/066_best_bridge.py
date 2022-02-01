"""
--- Best bridge ---
Write a function, best_bridge, that takes in a grid as an argument. The grid contains water (W) and land (L). There are exactly two islands in the grid. An island is a vertically or horizontally connected region of land. Return the minimum length bridge needed to connect the two islands. A bridge does not need to form a straight line.
"""


from collections import deque
import unittest


def best_bridge(grid):

    # Find start position
    start = None
    for ridx, row in enumerate(grid):
        if start:
            break
        for cidx, val in enumerate(row):
            if val == "L":
                start = (ridx, cidx)
                break

    # Build an island from start position
    island = set()
    stack = [start]
    while stack:
        r, c = stack.pop()
        row_inbounds = 0 <= r < len(grid)
        col_inbounds = 0 <= c < len(grid[0])
        if not row_inbounds or not col_inbounds:
            continue
        if grid[r][c] == "W":
            continue
        if (r, c) in island:
            continue

        island.add((r, c))
        stack.append((r + 1, c))
        stack.append((r - 1, c))
        stack.append((r, c + 1))
        stack.append((r, c - 1))

    # Use breath first search to find shortest path to other island
    best_bridge = float("inf")
    for cell in island:
        stack = deque([(*cell, 0)])
        visited = set().union(island)
        while stack:
            r, c, dist = stack.popleft()
            if (r, c) not in visited and grid[r][c] == "L":
                best_bridge = min(best_bridge, dist - 1)
                break

            visited.add((r, c))

            for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ri = r + i
                cj = c + j
                row_inbounds = 0 <= ri < len(grid)
                col_inbounds = 0 <= cj < len(grid[0])
                if not row_inbounds or not col_inbounds:
                    continue
                if (ri, cj) in visited:
                    continue

                stack.append((ri, cj, dist + 1))

    return best_bridge


class Test(unittest.TestCase):
    def test_00(self):
        grid = [
            ["W", "W", "W", "L", "L"],
            ["L", "L", "W", "W", "L"],
            ["L", "L", "L", "W", "L"],
            ["W", "L", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
        ]
        assert best_bridge(grid) == 1

    def test_01(self):
        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["L", "L", "W", "W", "L"],
            ["W", "L", "W", "W", "L"],
            ["W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W"],
        ]
        assert best_bridge(grid) == 2

    def test_02(self):
        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "L", "W"],
            ["L", "W", "W", "W", "W"],
        ]
        assert best_bridge(grid) == 3

    def test_03(self):
        grid = [
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "L", "W"],
            ["W", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "L", "L", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        assert best_bridge(grid) == 3

    def test_04(self):
        grid = [
            ["L", "L", "L", "L", "L", "L", "L", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "L", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "W", "W", "W", "W", "W", "W", "L"],
            ["L", "L", "L", "L", "L", "L", "L", "L"],
        ]
        assert best_bridge(grid) == 2

    def test_05(self):
        grid = [
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W", "W", "W", "L"],
        ]
        assert best_bridge(grid) == 8


if __name__ == "__main__":
    unittest.main()
