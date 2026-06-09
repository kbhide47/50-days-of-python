# Day 47: Graph Basics, BFS and DFS

from collections import deque

# Graph Representation
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

# Q1: Print Graph
print("Graph:")
for node in graph:
    print(node, "->", graph[node])

print("---------------------------")

# Q2: Count Vertices
print("Total Vertices:", len(graph))

print("---------------------------")

# Q3: Count Edges
edges = 0

for node in graph:
    edges += len(graph[node])

print("Total Edges:", edges // 2)

print("---------------------------")

# Q4: Check if Node Exists
node = input("Enter node to search: ")

if node in graph:
    print("Node Exists")
else:
    print("Node Not Found")

print("---------------------------")

# Q5: Display Neighbors
node = input("Enter node: ")

if node in graph:
    print("Neighbors:", graph[node])
else:
    print("Node Not Found")

print("---------------------------")

# Q6: BFS Traversal
def bfs(graph, start):

    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:

        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, "A")

print("\n---------------------------")

# Q7: DFS Traversal
def dfs(graph, node, visited):

    if node not in visited:

        print(node, end=" ")
        visited.add(node)

        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

print("DFS Traversal:")
dfs(graph, "A", set())

print("\n---------------------------")

# Q8: Check Path Exists
def has_path(graph, start, end, visited):

    if start == end:
        return True

    visited.add(start)

    for neighbor in graph[start]:

        if neighbor not in visited:

            if has_path(graph, neighbor, end, visited):
                return True

    return False

start = input("Start Node: ")
end = input("End Node: ")

print("Path Exists:", has_path(graph, start, end, set()))

print("---------------------------")

# Q9: Degree of a Node
node = input("Enter node: ")

if node in graph:
    print("Degree:", len(graph[node]))
else:
    print("Node Not Found")

print("---------------------------")

# Q10: Find All Nodes Reachable from Start
def reachable_nodes(graph, start):

    visited = set()

    def dfs_visit(node):

        visited.add(node)

        for neighbor in graph[node]:

            if neighbor not in visited:
                dfs_visit(neighbor)

    dfs_visit(start)

    return visited

start = input("Enter start node: ")

print("Reachable Nodes:", reachable_nodes(graph, start))
