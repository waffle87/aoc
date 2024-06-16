import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "data/12_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

g = []
for l in lines:
    g.append(l)
r = len(g)
c = len(g[0])
e = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        if g[i][j] == "S":
            e[i][j] = 1
        elif g[i][j] == "E":
            e[i][j] = 26
        else:
            e[i][j] = ord(g[i][j]) - ord("a") + 1


def bfs(part):
    q = deque()
    for i in range(r):
        for j in range(c):
            if (part == 1 and g[i][j] == "S") or (part == 2 and e[i][j] == 1):
                q.append(((i, j), 0))
    s = set()
    while q:
        (i, j), k = q.popleft()
        if (i, j) in s:
            continue
        s.add((i, j))
        if g[i][j] == "E":
            return k
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = i + dr
            cc = j + dc
            if 0 <= rr < r and 0 <= cc < c and e[rr][cc] <= 1 + e[i][j]:
                q.append(((rr, cc), k + 1))


print(bfs(1))
print(bfs(2))
