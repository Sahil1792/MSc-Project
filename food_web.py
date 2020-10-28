from collections import defaultdict
import csv
import networkx as nx
import matplotlib.pyplot as plt

graph=defaultdict(list)
with open('test_1.csv') as infile:
    reader=csv.reader(infile)
    for row in reader:
        try:
            graph[row[0]].append(row[1])
        except IndexError:
            pass
# print(graph)

# Creation of tree from all edges
# Node and edges generation
def generate_full(graph):
    edges = []
    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for consumer in graph[node]:
            # if edge exists then append
            if node != consumer:
                edges.append((node, consumer))

    # Graph from list of tupiles
    G = nx.DiGraph()
    G.add_edges_from(edges)
    nx.draw(G, with_labels = True, arrows=True)
    plt.savefig("full_graph.png")
    print("Total number of nodes: ", int(G.number_of_nodes()))
    print("Total number of edges: ", int(G.number_of_edges()))
    # print("List of all nodes: ", list(G.nodes()))
    # print("List of all edges: ", list(G.edges(data = True)))
    # print("Degree for all nodes: ", dict(G.degree()))

generate_full(graph)