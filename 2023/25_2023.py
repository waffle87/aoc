import sys
import re
from copy import deepcopy
import math
from collections import defaultdict, Counter, deque
import networkx as nx
import heapq

D = open(sys.argv[1]).read().strip()
L = D.split("\n")
G = [[c for c in row] for row in L]
R = len(G)
C = len(G[0])
E = defaultdict(set)
for line in L:
    s, e = line.split(":")
    for y in e.split():
        E[s].add(y)
        E[y].add(s)
n = len(E)
G = nx.DiGraph()
for k, vs in E.items():
    for v in vs:
        G.add_edge(k, v, capacity=1.0)
        G.add_edge(v, k, capacity=1.0)
for x in [list(E.keys())[0]]:
    for y in E.keys():
        if x != y:
            cut_val, (L, R) = nx.minimum_cut(G, x, y)
            if cut_val == 3:
                print(len(L) * len(R))
