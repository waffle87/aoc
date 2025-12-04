import heapq

input = "data/16_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
rows = len(lines)
cols = len(lines[0])
lines = [[lines[r][c] for c in range(cols)] for r in range(rows)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for r in range(rows):
    for c in range(cols):
        if lines[r][c] == "S":
            sr, sc = r, c
        if lines[r][c] == "E":
            er, ec = r, c


q = []
vis = set()
heapq.heappush(q, (0, sr, sc, 1))
dist = {}
best = None
while q:
    d, r, c, dir = heapq.heappop(q)
    if (r, c, dir) not in dist:
        dist[(r, c, dir)] = d
    if r == er and c == ec and best is None:
        best = d
    if (r, c, dir) in vis:
        continue
    vis.add((r, c, dir))
    dr, dc = dirs[dir]
    rr, cc = r + dr, c + dc
    if 0 <= cc < cols and 0 <= rr < rows and lines[rr][cc] != "#":
        heapq.heappush(q, (d + 1, rr, cc, dir))
    heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))


print(best)


q = []
vis = set()
dist2 = {}
for dir in range(4):
    heapq.heappush(q, (0, er, ec, dir))


while q:
    d, r, c, dir = heapq.heappop(q)
    if (r, c, dir) not in dist2:
        dist2[(r, c, dir)] = d
    if (r, c, dir) in vis:
        continue
    vis.add((r, c, dir))
    dr, dc = dirs[(dir + 2) % 4]
    rr, cc = r + dr, c + dc
    if 0 <= cc < cols and 0 <= rr < rows and lines[rr][cc] != "#":
        heapq.heappush(q, (d + 1, rr, cc, dir))
    heapq.heappush(q, (d + 1000, r, c, (dir + 1) % 4))
    heapq.heappush(q, (d + 1000, r, c, (dir + 3) % 4))


valid = set()
for r in range(rows):
    for c in range(cols):
        for dir in range(4):
            if (
                (r, c, dir) in dist
                and (r, c, dir) in dist2
                and dist[(r, c, dir)] + dist2[(r, c, dir)] == best
            ):
                valid.add((r, c))


print(len(valid))
