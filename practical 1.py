
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

def bfs(start):
    visited = []
    queue = []

    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)

        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



print("BFS Traversal:")
bfs('A')

