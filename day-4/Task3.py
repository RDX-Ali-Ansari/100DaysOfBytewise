from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend([n for n in graph[node] if n not in visited])

    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []

    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited

# Test the BFS and DFS functions
graph = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
bfs_result = bfs(graph, 2)
dfs_result = dfs(graph, 2)
print("BFS:", bfs_result)
print("DFS:", dfs_result)
