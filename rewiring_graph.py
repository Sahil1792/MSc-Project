from collections import defaultdict
import csv
import networkx as nx
import matplotlib.pyplot as plt

graph=defaultdict(list)
with open("test_1.csv") as infile:
    reader=csv.reader(infile)
    for row in reader:
        try:
            graph[row[0]].append(row[1])
        except IndexError:
            pass
# print(graph)

# Node and edges generation
def generate_edges(graph):
    edges = []
    # for each node in graph
    for node in graph:

        # for each neighbour node of a single node
        for consumer in graph[node]:
            # if edge exists then append
            if node != consumer:
                edges.append((node, consumer))

    return edges
# a=generate_edges(graph)

def rewire_edges():
    links = generate_edges(graph)
    # print(links)
    prey_list = set([lis[0] for lis in links])
    pred_list=set([lis[1] for lis in links])
    # print(pred_list)
    rewire_list=[]
    for li in pred_list:
        for position in links:
            for check in links:
                if (position[0] == li and position[1] == check[1]):
                    rewire_list.append((li, check[0]))

    list= [(a, b) for a, b in rewire_list if a != b]
    data = {tuple(item) for item in map(sorted, list)}

    return data


a=rewire_edges()

G = nx.DiGraph()
G.add_edges_from(a)
nx.draw(G, with_labels = True, arrows=True)
plt.savefig("rewire.png")

print("Total number f nodes: ", int(G.number_of_nodes()))
print("Total number og edges: ", int(G.number_of_edges()))
# print("List of all nodes: ", list(G.nodes()))
print("List of all edges: ", list(G.edges()))
# print("Degree for all nodes: ", dict(G.degree()))





