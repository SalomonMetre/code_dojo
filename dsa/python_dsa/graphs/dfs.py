
def dfs(graph, source, destination, path=None):
    if path is None:
        path = []
    path.append(source)
    if source == destination:
        return path
    for neighbour in graph.get(source, []):
        if neighbour not in path:
            result = dfs(graph, neighbour, destination, path)
            if result:
                return result
    path.pop()
    return None

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(dfs(graph, 'A', 'F'))
