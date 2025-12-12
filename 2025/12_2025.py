input = open("data/12_2025.txt").read()
data = input.split("\n\n")
presents, sizes = data[:-1], {}

for i in presents:
    lines = i.splitlines()
    name = int(lines[0][:-1])
    g = [list(row) for row in lines[1:]]
    size = 0
    for r in g:
        for c in r:
            if c == "#":
                size += 1
    sizes[name] = size

res, regions = 0, data[-1]
for i in regions.splitlines():
    sz, ns = i.split(": ")
    r, c = [int(x) for x in sz.split("x")]
    ns = [int(x) for x in ns.split()]
    total_ps = sum(k * sizes[j] for j, k in enumerate(ns))
    total_gs = r * c
    if total_ps * 1.3 < total_gs:
        res += 1
    elif total_ps > total_gs:
        pass

print(res)
