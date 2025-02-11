def dfs(graph, start_pt):
    stack = [start_pt]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node)
            stack.extend(graph.get(node, []))
