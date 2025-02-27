matrix = [
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0]
]

def matrix_edges_to_dict(edges):
    directed = defaultdict(set)

    for row in edges:
        for col in edges[row]:
            if directed[row][col] == 1:
                directed[row].add(col)
                # directed[col].add(row)
