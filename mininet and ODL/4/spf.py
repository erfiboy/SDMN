import networkx as nx


def create_network(matrix_size, adj_mat):
    G = nx.DiGraph()
    for i in range(0, matrix_size): 
        G.add_node(i+1)

    for i in range(1, matrix_size+1):
        for j in range(1, matrix_size+1):
            if adj_mat[i-1][j-1] == 0:
                continue
            G.add_edge( i,j, weight=adj_mat[i-1][j-1])

    return G


def find_shortest_path(matrix_size, adj_mat):
    G = create_network(matrix_size, adj_mat)
    shortest_path_1_n = nx.dijkstra_path(G, 1, matrix_size)
    shortest_path_n_1 = nx.dijkstra_path(G, matrix_size, 1)
    return shortest_path_1_n, shortest_path_n_1
