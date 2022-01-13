from collections import defaultdict, deque


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}


def dfs(graph):

    visited = set()
    largest_component = 0

    for start in graph:
        if start in visited:
            continue

        stack = [start]
        component = set()
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            component.add(node)
            stack += graph[node]

        if len(component) > largest_component:
            largest_component = len(component)

    return largest_component


def dfs_recursive(graph):

    visited = set()
    largest_component = 0

    for node in graph:
        if node in visited:
            continue
        count = explore(graph, node, visited)
        if count > largest_component:
            largest_component = count

    return largest_component


def explore(graph, src, visited, count=0):
    visited.add(src)
    count += 1
    for node in graph[src]:
        if node in visited:
            continue
        count = explore(graph, node, visited, count)
    return count


if __name__ == '__main__':
    assert dfs(graph) == 4
    assert dfs_recursive(graph) == 4
