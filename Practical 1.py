print("Anshrah Shaikh \nTYCS \nAI Prarctical 1")


from collections import deque

mumbai_map = {
    'Bhavans College': ['Azad Nagar Metro', 'SV Road'],

    # Metro Route
    'Azad Nagar Metro': ['DN Nagar Metro'],
    'DN Nagar Metro': ['Western Express Highway Metro'],
    'Western Express Highway Metro': ['Mithibai College'],

    # Road Route
    'SV Road': ['Juhu Circle'],
    'Juhu Circle': ['Mithibai College'],

    # Destination
    'Mithibai College': []
}

# ~~~~~~
# BFS
# ~~~~~~
def bfs_shortest_path(graph, start, destination):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored_count = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored_count += 1

        if current == destination:
            return path, nodes_explored_count

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored_count

# ~~~~~~
# DFS
# ~~~~~~
def iterative_dfs_path(graph, start, destination):
    stack = [(start, [start])]
    visited = set()
    nodes_explored_count = 0

    while stack:
        current, path = stack.pop()
        nodes_explored_count += 1

        if current == destination:
            return path, nodes_explored_count

        if current not in visited:
            visited.add(current)

            for neighbor in reversed(graph.get(current, [])):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored_count

# ~~~~`mAIN FUNCTION~~~~~~
start_node = "Bhavans College"
end_node = "Mithibai College"

bfs_path, bfs_count = bfs_shortest_path(mumbai_map, start_node, end_node)
dfs_path, dfs_count = iterative_dfs_path(mumbai_map, start_node, end_node)

print("----- BFS Results -----")
print("Path Found:", " -> ".join(bfs_path))
print("Total Steps (Edges):", len(bfs_path) - 1)
print("Total Nodes Visited:", bfs_count)

print("\n----- DFS Results -----")
print("Path Found:", " -> ".join(dfs_path))
print("Total Steps (Edges):", len(dfs_path) - 1)
print("Total Nodes Visited:", dfs_count)