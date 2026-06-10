# Day 48: Advanced Graph Problems

from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 4],
    3: [1],
    4: [2]
}

# Q1: BFS Traversal
def bfs(start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS:")
bfs(0)

print("\n---------------------------")

# Q2: DFS Traversal
def dfs(node, visited):

    visited.add(node)

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:
            dfs(neighbor, visited)

print("DFS:")
dfs(0, set())

print("\n---------------------------")

# Q3: Shortest Path using BFS
def shortest_path(start, end):

    queue = deque([(start, [start])])

    visited = set()

    while queue:

        node, path = queue.popleft()

        if node == end:
            return path

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

print("Shortest Path 0 → 4:")
print(shortest_path(0, 4))

print("---------------------------")

# Q4: Count Connected Components
graph2 = {
    0: [1],
    1: [0],
    2: [3],
    3: [2],
    4: []
}

visited = set()

def dfs_component(node):

    visited.add(node)

    for neighbor in graph2[node]:

        if neighbor not in visited:
            dfs_component(neighbor)

count = 0

for node in graph2:

    if node not in visited:
        dfs_component(node)
        count += 1

print("Connected Components:", count)

print("---------------------------")

# Q5: Detect Cycle (Undirected Graph)
graph3 = {
    0: [1],
    1: [0, 2],
    2: [1, 3],
    3: [2, 1]
}

def has_cycle(node, visited, parent):

    visited.add(node)

    for neighbor in graph3[node]:

        if neighbor not in visited:

            if has_cycle(neighbor, visited, node):
                return True

        elif parent != neighbor:
            return True

    return False

print("Cycle Exists:",
      has_cycle(0, set(), -1))

print("---------------------------")

# Q6: Degree of Every Node
for node in graph:

    print("Node", node,
          "Degree =", len(graph[node]))

print("---------------------------")

# Q7: Find All Reachable Nodes
def reachable(start):

    visited = set()

    def dfs_visit(node):

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)

    return visited

print("Reachable from 0:",
      reachable(0))

print("---------------------------")

# Q8: Check Path Exists
def path_exists(start, end):

    visited = set()

    def dfs(node):

        if node == end:
            return True

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:

                if dfs(neighbor):
                    return True

        return False

    return dfs(start)

print("Path Exists 0→4:",
      path_exists(0, 4))

print("---------------------------")

# Q9: Count Total Edges
edges = 0

for node in graph:
    edges += len(graph[node])

print("Total Edges:",
      edges // 2)

print("---------------------------")

# Q10: Graph Adjacency Matrix
size = len(graph)

matrix = [[0] * size for _ in range(size)]

for node in graph:

    for neighbor in graph[node]:
        matrix[node][neighbor] = 1

print("Adjacency Matrix:")

for row in matrix:
    print(row)
