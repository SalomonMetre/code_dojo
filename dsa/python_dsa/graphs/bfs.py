from collections import deque

def bfs(graph: dict, source: str, destination: str):
    visited = set()
    search_queue = deque()
    parents = {}
    path = []
    search_queue.append(source)
    while search_queue:
        dequeued_vertex = search_queue.popleft()
        visited.add(dequeued_vertex)
        if dequeued_vertex == destination:
            break
        for neighbour in graph.get(dequeued_vertex, []):
            if neighbour not in visited:
                parents[neighbour] = dequeued_vertex
                search_queue.append(neighbour)
    step = destination
    while step is not None:
        path.append(step)
        step = parents.get(step)
    return path[::-1]


# graph 1
graph1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['C', 'D', 'E']
}

print(bfs(graph=graph1, source='C', destination='E'))