from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph
import networkx as nx

edges = [(1, 2), (2, 3), (3, 4), (1, 5), (5, 6), (6, 7)]
G = create_graph(edges)
print(G.edges)  

G = nx.Graph(edges)

degree = get_degree(G, 2)

# Menghitung derajat node 2
print("Derajat node 2:", get_degree(G, 2))  

# Traversal DFS mulai dari node 1
print("DFS traversal dari node 1:", dfs_traversal(G, 1)) 

# Traversal BFS mulai dari node 1
print("BFS traversal dari node 1:", bfs_traversal(G, 1)) 

# Mencari jalur terpendek dari node 1 ke node 7
print("Jalur terpendek dari node 1 ke 7:", find_shortest_path(G, 1, 7)) 

visualize_graph(G)