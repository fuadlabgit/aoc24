import numpy as np 
import networkx as nx 
from itertools import combinations 

input = open("input.txt", "r").readlines()

G = nx.Graph()
G.add_edges_from([tuple(line.strip().split("-")) for line in input])

triples = set()
for n1 in G.nodes:
    nbrs = set(G[n1])
    for n2, n3 in combinations(nbrs,2):
        if (n2, n3) in G.edges:
            new_combi = tuple(sorted((n1,n2,n3)))
            if any([c.startswith("t") for c in new_combi]):
                triples.add(new_combi)
print(len(triples))
