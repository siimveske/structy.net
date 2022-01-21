from collections import defaultdict, deque


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


def build_graph(edges):
    graph = defaultdict(list)
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    return graph


def dfs(graph, start, end):

    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        if node == end:
            return True
        visited.add(node)
        stack += graph[node]

    return False


def dfs_rec(graph, start, end, visited=set()):

    if start == end:
        return True

    visited.add(start)

    for node in graph[start]:
        if node in visited:
            continue
        if dfs_rec(graph, node, end, visited):
            return True

    return False


if __name__ == '__main__':

    graph = build_graph(edges)
    assert dfs(graph, 'i', 'm')
    assert dfs_rec(graph, 'i', 'm')
