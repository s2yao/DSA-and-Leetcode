def bfs(graph, start):
    visited_set = set()
    queue = deque([start])

    while queue:
        curr = queue.popleft()
        if curr not in visited_set:
            visited_set.add(curr)
            for neighbor in graph[curr]:
                if neighbor not in visited_set:
                    queue.append(neighbor)

def dfs(graph, start_pt):
    visited_set = set()
    stack = [start_pt]

    while stack:
        curr = stack.pop()

        if curr not in visited_set:
            visited_set.add(curr)
            
            for neighbor in graph[curr]:
                if neighbor not in visited_set:
                    stack.append(neighbor)


def dfs(graph, start):
    visited_set = set()

    def traversal(node):
        if node not in visited_set:
            visited_set.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited_set:
                traversal(neighbor)
    traversal(start)
