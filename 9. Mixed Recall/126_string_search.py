"""
--- String search ---
Write a function, string_search, that takes in a grid of letters and a string as arguments. The function should return a boolean indicating whether or not the string can be found in the grid as a path by connecting horizontal or vertical positions. The path can begin at any position, but you cannot reuse a position more than once in the path.

You can assume that all letters are lowercase and alphabetic.
"""
import unittest


def string_search(grid, s):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if dfs(grid, s, 0, row, col, set()):
                return True
    return False


def dfs(grid, s, idx, row, col, visited):
    if idx == len(s):
        return True

    row_inbounds = 0 <= row < len(grid)
    col_inbounds = 0 <= col < len(grid[0])
    if not row_inbounds or not col_inbounds:
        return False

    if grid[row][col] != s[idx]:
        return False

    key = (row, col)
    visited.add(key)

    up = (row + 1, col)
    down = (row - 1, col)
    left = (row, col - 1)
    right = (row, col + 1)
    directions = [up, down, left, right]
    for new_row, new_col in directions:
        if (new_row, new_col) in visited:
            continue
        if dfs(grid, s, idx + 1, new_row, new_col, visited):
            return True

    return False


class Test(unittest.TestCase):
    def test_00(self):
        grid = [
            ['e', 'y', 'h', 'i', 'j'],
            ['q', 'x', 'e', 'r', 'p'],
            ['r', 'o', 'l', 'l', 'n'],
            ['p', 'r', 'x', 'o', 'h'],
            ['a', 'a', 'm', 'c', 'm']
        ]
        assert string_search(grid, 'hello') == True

    def test_01(self):
        grid = [
            ['e', 'y', 'h', 'i', 'j'],
            ['q', 'x', 'e', 'r', 'p'],
            ['r', 'o', 'l', 'l', 'n'],
            ['p', 'r', 'x', 'o', 'h'],
            ['a', 'a', 'm', 'c', 'm']
        ]
        assert string_search(grid, 'proxy') == True

    def test_02(self):
        grid = [
            ['e', 'y', 'h', 'i', 'j'],
            ['q', 'x', 'e', 'r', 'p'],
            ['r', 'o', 'l', 'l', 'n'],
            ['p', 'r', 'x', 'o', 'h'],
            ['a', 'a', 'm', 'c', 'm']
        ]
        assert string_search(grid, 'rolling') == False

    def test_03(self):
        grid = [
            ['e', 'y', 'h', 'i', 'j'],
            ['q', 'x', 'e', 'r', 'p'],
            ['r', 'o', 'l', 'l', 'n'],
            ['p', 'r', 'x', 'o', 'h'],
            ['a', 'a', 'm', 'z', 'm']
        ]
        assert string_search(grid, 'zoo') == False

    def test_04(self):
        grid = [
            ['q', 'w', 'h', 'i', 'j'],
            ['q', 'e', 'r', 'o', 'p'],
            ['h', 'y', 't', 'x', 'z'],
            ['k', 'o', 'm', 'o', 'p']
        ]
        assert string_search(grid, 'qwerty') == True

    def test_05(self):
        grid = [
            ['f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p'],
            ['o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v'],
            ['g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n'],
            ['a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm'],
            ['m', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c'],
            ['q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z'],
            ['d', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k'],
            ['f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w'],
            ['p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i'],
            ['l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q']
        ]
        assert string_search(grid, 'paprika') == True

    def test_06(self):
        grid = [
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x'],
            ['s', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h'],
        ]
        assert string_search(grid, 'ssssssssssh') == False


if __name__ == "__main__":
    unittest.main()
