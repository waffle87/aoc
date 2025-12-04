import re
from collections import deque

input = "data/14_2024.txt"
data = open(input).read().strip()
x, y, robots = 101, 103, []
q1, q2, q3, q4 = 0, 0, 0, 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


for line in data.split("\n"):
    px, py, vx, vy = ints(line)
    robots.append((px, py, vx, vy))


for t in range(1, 10**6):
    g = [["." for x in range(x)] for y in range(y)]
    if t == 100:
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        mx = x // 2
        my = y // 2
    for i, (px, py, vx, vy) in enumerate(robots):
        px += vx
        py += vy
        px %= x
        py %= y
        robots[i] = (px, py, vx, vy)
        assert 0 <= px < x
        assert 0 <= py < y
        g[py][px] = "#"

        if t == 100:
            if px < mx and py < my:
                q1 += 1
            if px > mx and py < my:
                q2 += 1
            if px < mx and py > my:
                q3 += 1
            if px > mx and py > my:
                q4 += 1
    if t == 100:
        print(q1 * q2 * q3 * q4)
    components = 0
    vis = set()
    for x in range(x):
        for y in range(y):
            if g[y][x] == "#" and (x, y) not in vis:
                sx, sy = x, y
                components += 1
                q = deque([(sx, sy)])
                while q:
                    x2, y2 = q.popleft()
                    if (x2, y2) in vis:
                        continue
                    vis.add((x2, y2))
                    for dx, dy in dirs:
                        xx, yy = x2 + dx, y2 + dy
                        if 0 <= xx < x and 0 <= yy < y and g[yy][xx] == "#":
                            q.append((xx, yy))
    if components <= 200:
        print(t)
        gstr = []
        for row in g:
            gstr.append("".join(row))
        print("\n".join(gstr))
        break
