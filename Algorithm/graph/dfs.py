def dfs(graph, start_pt):
    stack = [start_pt]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)

# Recursion approach
def dfs(graph, start):
    visited = set()
    
    def dfs_visit(node):
        if node not in visited:
            print(node)  # Process the node
            visited.add(node)
            for neighbor in graph[node]:
                dfs_visit(neighbor)
    
    dfs_visit(start)