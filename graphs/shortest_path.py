from collections import defaultdict, deque

'''
https://structy.net/problems/island-count
https://www.youtube.com/watch?v=tWVWeAqZ0WU&t=5976s
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
    ['W', 'W'],
    ['W', 'W'],
]


def build_graph(edges):
    graph = defaultdict(list)
    rows = len(edges)
    cols = len(edges[0])
    for i in range(rows):
        for j in range(cols):
            top = (i-1, j)
            right = (i, j+1)
            btm = (i+1, j)
            left = (i, j-1)
            neighbors = [top, right, btm, left]

            for neighbor in neighbors:
                ni, nj = neighbor
                if (ni >= 0 and ni < rows) and (nj >= 0 and nj < cols):
                    graph[(i, j, edges[i][j])].append((ni, nj, edges[ni][nj]))
    return graph


def islandCount(grid):
    graph = build_graph(grid)
    visited = set()
    island_count = 0

    for start in graph:
        if start in visited or start[2] == 'W':
            continue

        queue = deque([start])
        while queue:
            node = queue.popleft()
            if node in visited or node[2] == 'W':
                continue
            visited.add(node)
            queue += graph[node]
        island_count += 1

    return island_count


def explore(grid, row, col, visited):
    rowInbound = 0 <= row <= len(grid)
    colInboud = 0 <= col <= len(grid[0])

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


def islandCount2(grid):
    visited = set()
    island_count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):
                island_count += 1
    return island_count


if __name__ == '__main__':

    assert islandCount(grid1) == 3
    assert islandCount(grid2) == 4
    assert islandCount(grid3) == 1
    assert islandCount(grid4) == 0

    assert islandCount2(grid1) == 3
    assert islandCount2(grid2) == 4
    assert islandCount2(grid3) == 1
    assert islandCount2(grid4) == 0

    print('OK')
