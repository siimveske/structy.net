'''
https://structy.net/problems/minimum-island
https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=7132s
'''

grid1 = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

grid2 = [
    ['L', 'W', 'W', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['W', 'L', 'W', 'L', 'W'],
    ['W', 'W', 'W', 'W', 'W'],
    ['W', 'W', 'L', 'L', 'L'],
]

grid3 = [
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
    ['L', 'L', 'L'],
]

grid4 = [
    ['W', 'W'],
    ['L', 'L'],
    ['W', 'W'],
    ['W', 'L'],
]


def explore(grid, row, col, visited):
    row_inbound = 0 <= row < len(grid)
    col_inboud = 0 <= col < len(grid[0])

    if not row_inbound or not col_inboud:
        return 0
    if grid[row][col] == 'W':
        return 0
    if (row, col) in visited:
        return 0

    visited.add((row, col))

    size = 1
    size += explore(grid, row-1, col, visited)
    size += explore(grid, row+1, col, visited)
    size += explore(grid, row, col-1, visited)
    size += explore(grid, row, col+1, visited)

    return size


def minimum_island(grid):
    visited = set()
    result = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            island_size = explore(grid, row, col, visited)
            if island_size != 0 and island_size < result:
                result = island_size

    return result


if __name__ == '__main__':

    assert minimum_island(grid1) == 2
    assert minimum_island(grid2) == 1
    assert minimum_island(grid3) == 9
    assert minimum_island(grid4) == 1

    print('OK')
