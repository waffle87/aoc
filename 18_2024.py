from collections import deque

input = "data/18_2024.txt"
data = open(input).read().strip()
cnt = 71
v = [["." for c in range(cnt)] for r in range(cnt)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i, line in enumerate(data.split("\n")):
    x, y = [int(x) for x in line.split(",")]
    if 0 <= y < cnt and 0 <= x < cnt:
        v[y][x] = "#"
    q = deque([(0, 0, 0)])
    vis, ok = set(), False
    while q:
        d, r, c = q.popleft()
        if (r, c) == (cnt - 1, cnt - 1):
            if i == 1023:
                print(d)
            ok = True
            break
        if (r, c) in vis:
            continue
        vis.add((r, c))
        for dr, dc in dirs:
            rr = r + dr
            cc = c + dc
            if 0 <= rr < cnt and 0 <= cc < cnt and v[rr][cc] != "#":
                q.append((d + 1, rr, cc))
    if not ok:
        print(f"{x},{y}")
        break
