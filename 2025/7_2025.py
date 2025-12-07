from collections import deque
from functools import cache

input = open("data/7_2025.txt").read()
grid = [list(i) for i in input.splitlines()]
r, c = len(grid), len(grid[0])

for i in range(r):
    for j in range(c):
        if grid[i][j] == "S":
            sr, sc = i, j


@cache
def score(x, y):
    if x + 1 == r:
        return 1
    if grid[x + 1][y] == "^":
        return score(x + 1, y - 1) + score(x + 1, y + 1)
    else:
        return score(x + 1, y)


p1, vis = 0, set()
q = deque([(sr, sc)])
while q:
    x, y = q.popleft()
    if (x, y) in vis:
        continue
    vis.add((x, y))
    if x + 1 == r:
        continue
    if grid[x + 1][y] == "^":
        q.append((x + 1, y - 1))
        q.append((x + 1, y + 1))
        p1 += 1
    else:
        q.append((x + 1, y))

p2 = score(sr, sc)

print(p1)
print(p2)
