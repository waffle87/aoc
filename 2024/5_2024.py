import sys
from pyperclip import copy
from collections import defaultdict, deque

input = "data/5_2024.txt"
data = open(input).read().strip()
edges, queries = data.split("\n\n")
sys.setrecursionlimit(10**6)
p1, p2 = 0, 0
prev = defaultdict(set)
past = defaultdict(set)

for line in edges.split("\n"):
    x, y = line.split("|")
    x, y = int(x), int(y)
    prev[y].add(x)
    past[x].add(y)

for query in queries.split("\n"):
    vs = [int(x) for x in query.split(",")]
    assert len(vs) % 2 == 1
    ok = True
    for i, x in enumerate(vs):
        for j, y in enumerate(vs):
            if i < j and y in prev[x]:
                ok = False
    if ok:
        p1 += vs[len(vs) // 2]
    else:
        good, q = [], deque([])
        data = {v: len(prev[v] & set(vs)) for v in vs}
        for v in vs:
            if data[v] == 0:
                q.append(v)
        while q:
            x = q.popleft()
            good.append(x)
            for y in past[x]:
                if y in data:
                    data[y] -= 1
                    if data[y] == 0:
                        q.append(y)
        p2 += good[len(good) // 2]


def solve(s):
    print(s)
    copy(s)


solve(p1)
solve(p2)
