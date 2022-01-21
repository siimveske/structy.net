'''
https://structy.net/problems/island-count
https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=5976s
'''


def explore(grid, row, col, visited):
    rowInbound = 0 <= row < len(grid)
    colInboud = 0 <= col < len(grid[0])

    if not rowInbound or not colInboud:
        return False
    if grid[row][col] == 'W':
        return False
    if (row, col) in visited:
        return False

    visited.add((row, col))

    explore(grid, row-1, col, visited)
    explore(grid, row+1, col, visited)
    explore(grid, row, col-1, visited)
    explore(grid, row, col+1, visited)

    return True


def island_count(grid):
    visited = set()
    island_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                island_count += 1
    return island_count


if __name__ == '__main__':
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]
    assert island_count(grid) == 3

    grid = [
        ['L', 'W', 'W', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'L', 'W', 'L', 'W'],
        ['W', 'W', 'W', 'W', 'W'],
        ['W', 'W', 'L', 'L', 'L'],
    ]
    assert island_count(grid) == 4

    grid = [
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
        ['L', 'L', 'L'],
    ]
    assert island_count(grid) == 1

    grid = [
        ['W', 'W'],
        ['W', 'W'],
        ['W', 'W'],
    ]
    assert island_count(grid) == 0

    print('OK')
