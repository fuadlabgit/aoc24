import sys 
import numpy as np 
import networkx as nx 
from itertools import combinations 

input = open("input.txt", "r").readlines()

G = nx.Graph()
G.add_edges_from([tuple(line.strip().split("-")) for line in input])
# print(len(G.nodes), "nodes", len(G.edges), "edges")

def expand(nodes, new_node):
    for n in nodes: # check if this node is connected to all others
        if new_node not in G[n]: break 
    else: return True 
    return False #

maxlen = 0
best = None 

# check connectedness for each node and record largest connected group
for start in G.nodes:
    nodes = set([start])
    q = set(nodes)
    while q:
        n = q.pop()
        for nxt in G[n]:
            success = expand(nodes, nxt)
            if success:
                q.add(nxt)
                nodes.add(nxt)
    nodes = sorted(nodes)
    
    if len(nodes) > maxlen:
        maxlen = len(nodes)
        best = nodes 

print(",".join(best))
