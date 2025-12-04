import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "data/9_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]


def adjust(h, t):
    dr = h[0] - t[0]
    dc = h[1] - t[1]
    if abs(dr) <= 1 and abs(dc) <= 1:
        pass
    elif abs(dr) >= 2 and abs(dc) >= 2:
        t = (
            h[0] - 1 if t[0] < h[0] else h[0] + 1,
            h[1] - 1 if t[1] < h[1] else h[1] + 1,
        )
    elif abs(dr) >= 2:
        t = (h[0] - 1 if t[0] < h[0] else h[0] + 1, h[1])
    elif abs(dc) >= 2:
        t = (h[0], h[1] - 1 if t[1] < h[1] else h[1] + 1)
    return t


h = (0, 0)
t = [(0, 0) for _ in range(9)]
dr = {"L": 0, "U": -1, "R": 0, "D": 1}
dc = {"L": -1, "U": 0, "R": 1, "D": 0}
p1 = set([t[0]])
p2 = set([t[8]])
for l in lines:
    d, amt = l.split()
    amt = int(amt)
    for _ in range(amt):
        h = (h[0] + dr[d], h[1] + dc[d])
        t[0] = adjust(h, t[0])
        for i in range(1, 9):
            t[i] = adjust(t[i - 1], t[i])
        p1.add(t[0])
        p2.add(t[8])

print(len(p1))
print(len(p2))
