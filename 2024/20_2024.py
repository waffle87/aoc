from collections import deque

input = "data/20_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
rows, cols = len(lines), len(lines[0])
lines = [[lines[r][c] for c in range(cols)] for r in range(rows)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r in range(rows):
    for c in range(cols):
        if lines[r][c] == "S":
            sr, sc = r, c
        if lines[r][c] == "E":
            er, ec = r, c

dist, q = {}, deque([(0, er, ec)])
while q:
    d, r, c = q.popleft()
    if (r, c) in dist:
        continue
    dist[(r, c)] = d
    for dr, dc in dirs:
        rr, cc = r + dr, c + dc
        if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] != "#":
            q.append((d + 1, rr, cc))


def find_cheat(d0, cheat_time):
    q = deque([(0, None, None, None, sr, sc)])
    res, vis, keep = set(), set(), 100
    while q:
        d, cheat_start, cheat_end, cheat_time, r, c = q.popleft()
        assert cheat_end is None
        if d >= d0 - keep:
            continue
        if lines[r][c] == "E":
            if cheat_end is None:
                cheat_end = (r, c)
            if d <= d0 - keep and (cheat_start, cheat_end) not in res:
                res.add((cheat_start, cheat_end))
        if (r, c, cheat_start, cheat_end, cheat_time) in vis:
            continue
        vis.add((r, c, cheat_start, cheat_end, cheat_time))
        if cheat_start is None:
            assert lines[r][c] != "#"
            q.append((d, (r, c), None, cheat_time, r, c))
        if cheat_time is not None and lines[r][c] != "#":
            assert lines[r][c] in [".", "S", "E"]
            if dist[(r, c)] <= d0 - 100 - d:
                res.add((cheat_start, (r, c)))
        if cheat_time == 0:
            continue
        else:
            for dr, dc in dirs:
                rr, cc = r + dr, c + dc
                if cheat_time is not None:
                    assert cheat_time > 0
                    if 0 <= rr < rows and 0 <= cc < cols:
                        q.append((d + 1, cheat_start, None, cheat_time - 1, rr, cc))
                else:
                    if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] != "#":
                        q.append((d + 1, cheat_start, cheat_end, cheat_time, rr, cc))
    return len(res)


d0 = dist[(sr, sc)]
print(find_cheat(d0, 2))
print(find_cheat(d0, 20))
