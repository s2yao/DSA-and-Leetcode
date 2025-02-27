edges = [[0, 1], [1, 2], [2, 0], [2, 3]]

# using set to store tuple
# O1 looking up edge
def directed_graph_from_edges_set(edges):
    directed = set()

    for edge in edges:
        directed.add((edge[0], edge[1]))
    
directed_graph_from_edges(edges)

# using dictionary to store value
# O1 looking up edges connecting the current node
def directed_graph_from_edges_set(edges):
    directed = defaultdict(list)

    for edge in edges:
        directed[edge[0]].append(edge[1])



# How about undirected?

