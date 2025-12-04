from collections import deque

input = "data/12_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
rows = len(lines)
cols = len(lines[0])
p1, p2, vis = 0, 0, set()
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for r in range(rows):
    for c in range(cols):
        if (r, c) in vis:
            continue
        q, dic = deque([(r, c)]), dict()
        area, perim = 0, 0
        while q:
            r2, c2 = q.popleft()
            if (r2, c2) in vis:
                continue
            vis.add((r2, c2))
            area += 1
            for dr, dc in dirs:
                rr = r2 + dr
                cc = c2 + dc
                if 0 <= rr < rows and 0 <= cc < cols and lines[rr][cc] == lines[r2][c2]:
                    q.append((rr, cc))
                else:
                    perim += 1
                    if (dr, dc) not in dic:
                        dic[(dr, dc)] = set()
                    dic[(dr, dc)].add((r2, c2))
        sides = 0
        for k, vs in dic.items():
            vis_dic = set()
            for pr, pc in vs:
                if (pr, pc) not in vis_dic:
                    sides += 1
                    q = deque([(pr, pc)])
                    while q:
                        r2, c2 = q.popleft()
                        if (r2, c2) in vis_dic:
                            continue
                        vis_dic.add((r2, c2))
                        for dr, dc in dirs:
                            rr, cc = r2 + dr, c2 + dc
                            if (rr, cc) in vs:
                                q.append((rr, cc))
        p1 += area * perim
        p2 += area * sides


print(p1)
print(p2)
