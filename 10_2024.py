from collections import deque

input = "data/10_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
lines = [[int(x) for x in row] for row in lines]
rows, cols = len(lines), len(lines[0])
p1, p2, dp = 0, 0, {}


def ways0(sr, sc):
    q = deque([(sr, sc)])
    res, vis = 0, set()
    while q:
        r, c = q.popleft()
        if (r, c) in vis:
            continue
        vis.add((r, c))
        if lines[r][c] == 0:
            res += 1
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] == lines[r][c] - 1:
                q.append((rr, cc))
    return res


def ways1(r, c):
    if lines[r][c] == 0:
        return 1
    if (r, c) in dp:
        return dp[(r, c)]
    res = 0
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        rr = r + dr
        cc = c + dc
        if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] == lines[r][c] - 1:
            res += ways1(rr, cc)
    dp[(r, c)] = res
    return res


for r in range(rows):
    for c in range(cols):
        if lines[r][c] == 9:
            p1 += ways0(r, c)
            p2 += ways1(r, c)

print(p1)
print(p2)
