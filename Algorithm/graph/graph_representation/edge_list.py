edges = [[0, 1], [1, 2], [2, 0], [2, 3]]

# using set to store tuple
# O1 looking up edge
def directed_graph_from_edges_set(edges):
    directed = set()

    for u, v in edges:
        directed.add((u, v))
        # directed.add((v, u))

# using dictionary to store value
# O1 looking up edges connecting the current node
def directed_graph_from_edges_set(edges):
    directed = defaultdict(list)

    for u, v in edges:
        directed[u].add(v)
        # directed[v].add(u)


