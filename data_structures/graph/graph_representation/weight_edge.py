weighted_edges = [[0, 1, 2.5], [1, 2, 3.0], [2, 0, 1.2]]

def weighted_edges_to_dict(edges):
    directed = defaultdict(dict)

    for u, v, value in edges:
        directed[u][v] = value
        # directed[v][u] = -value