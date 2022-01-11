from collections import deque

graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def dfs(graph, start):
    path = []
    stack = [start]
    while stack:
        node = stack.pop()
        path.append(node)
        stack += graph[node]
    return path


def dfs_rec(graph, start, path=[]):

    path += [start]
    for node in graph[start]:
        dfs_rec(graph, node, path)

    return path


def bfs(graph, start):
    path = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        path.append(node)
        queue += graph[node]
    return path


def bfs_rec(graph: dict, queue: deque, path=[]):

    if not queue:
        return

    node = queue.popleft()
    path += [node]
    queue += graph[node]
    bfs_rec(graph, queue, path)

    return path


print(dfs(graph, 'a'))
print(bfs(graph, 'a'))

print(dfs_rec(graph, 'a'))
print(bfs_rec(graph, deque(['a'])))
