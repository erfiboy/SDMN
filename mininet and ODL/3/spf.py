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


def find_shortest_path(G, start, end):
    return nx.dijkstra_path(G, start, end)




matrix_size = int(input("Enter matrix size: "))
adj_mat = [[] for i in range(0,matrix_size)]

for i in range(0, matrix_size):
    for j in range(0, matrix_size):
        adj_mat[i].append(int(input()))

G = create_network(matrix_size, adj_mat)
print find_shortest_path(G, 1, matrix_size)
print find_shortest_path(G, matrix_size, 1)
