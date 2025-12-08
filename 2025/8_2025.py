from collections import defaultdict

input = open("data/8_2025.txt")
data = input.read().splitlines()
p, d = [], []

for i in data:
    x, y, z = [int(x) for x in i.split(",")]
    p.append((x, y, z))

for i, (x1, y1, z1) in enumerate(p):
    for j, (x2, y2, z2) in enumerate(p):
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
        if i > j:
            d.append((dist, i, j))

d = sorted(d)
uf = {i: i for i in range(len(p))}


def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]


def mix(x, y):
    uf[find(x)] = find(y)


connections = 0

for t, (x, y, z) in enumerate(d):
    if t == 1000:
        sz = defaultdict(int)
        for i in range(len(p)):
            sz[find(i)] += 1
        s = sorted(sz.values())
        print(s[-1] * s[-2] * s[-3])
    if find(y) != find(z):
        connections += 1
        if connections == len(p) - 1:
            print(p[y][0] * p[z][0])
        mix(y, z)
