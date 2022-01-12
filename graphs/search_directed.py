from collections import deque

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def dfs(graph, start, end):

    stack = [start]
    while stack:
        node = stack.pop()
        if node == end:
            return True
        stack += graph[node]
    return False


def bfs(graph, start, end):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        queue += graph[node]
    return False


def dfs_rec(graph, start, end):

    if start == end:
        return True

    for node in graph[start]:
        if dfs_rec(graph, node, end):
            return True

    return False


def undirectedPath(edges, nodeA, nodeB):
    pass


if __name__ == '__main__':
    assert dfs(graph, 'f', 'h')
    assert bfs(graph, 'f', 'h')
    assert dfs_rec(graph, 'f', 'h')
