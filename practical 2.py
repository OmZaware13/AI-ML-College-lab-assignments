graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3, 'E': 1},
    'C': {'F': 2},
    'D': {'G': 2},
    'E': {'G': 2},
    'F': {'G': 1},
    'G': {}
}
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 1,
    'G': 0
}
def a_star(start, goal):

    open_list = [start]
    visited = []

    cost = {start: 0}
    parent = {start: None}

    while open_list:
        current = open_list[0]

        for node in open_list:
            if cost[node] + h[node] < cost[current] + h[current]:
                current = node

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, cost[goal]

        open_list.remove(current)
        visited.append(current)

        for neighbour in graph[current]:

            if neighbour in visited:
                continue

            new_cost = cost[current] + graph[current][neighbour]

            if neighbour not in open_list:
                open_list.append(neighbour)

            if new_cost < cost.get(neighbour, 999):
                cost[neighbour] = new_cost
                parent[neighbour] = current

    return None, 0



print("A* ALGORITHM")
print("Available nodes: A, B, C, D, E, F, G")

start = input("Enter starting node: ").upper()
goal = input("Enter goal node: ").upper()

if start not in graph or goal not in graph:
    print("Invalid node!")
else:
    path, total_cost = a_star(start, goal)

    if path:
        print("\nPath:", " -> ".join(path))
        print("Total Cost:", total_cost)
    else:
        print("Path not found!")

