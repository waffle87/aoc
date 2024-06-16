import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "data/8_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

g = []
for line in lines:
    row = line
    g.append(row)

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
r = len(g)
c = len(g[0])
p1 = 0
p2 = 0

for i in range(r):
    for j in range(c):
        vis = False
        for dr, dc in dir:
            rr = i
            cc = j
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0 <= rr < r and 0 <= cc < c):
                    break
                if g[rr][cc] >= g[i][j]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1

for i in range(r):
    for j in range(c):
        score = 1
        for dr, dc in dir:
            dist = 1
            rr = i + dr
            cc = j + dc
            while True:
                if not (0 <= rr < r and 0 <= cc < c):
                    dist -= 1
                    break
                if g[rr][cc] >= g[i][j]:
                    break
                dist += 1
                rr += dr
                cc += dc
            score *= dist
        p2 = max(p2, score)
print(p1)
print(p2)
