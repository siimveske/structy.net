from collections import defaultdict, deque


graph = {
    3: [],
    4: [6],
    6: [4, 5, 7, 8],
    8: [6],
    7: [6],
    5: [6],
    1: [2],
    2: [1]
}


def dfs(graph):

    visited = set()
    count = 0

    for start in graph:
        if start in visited:
            continue
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack += graph[node]
        count += 1

    return count


def dfs_recursive(graph):

    visited = set()
    count = 0

    for node in graph:
        if node in visited:
            continue
        explore(graph, node, visited)
        count += 1

    return count


def explore(graph, src, visited):
    visited.add(src)
    for node in graph[src]:
        if node in visited:
            continue
        explore(graph, node, visited)


if __name__ == '__main__':
    assert dfs(graph) == 3
    assert dfs_recursive(graph) == 3
