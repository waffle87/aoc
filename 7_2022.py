import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "data/7_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

sz = defaultdict(int)
path = []
for line in lines:
    words = line.strip().split()
    if words[1] == "cd":
        if words[2] == "..":
            path.pop()
        else:
            path.append(words[2])
    elif words[1] == "ls":
        continue
    elif words[0] == "dir":
        continue
    else:
        j = int(words[0])
        for i in range(1, len(path) + 1):
            sz["/".join(path[:i])] += j

max_used = 70000000 - 30000000
total_used = sz["/"]
need_free = total_used - max_used

p1 = 0
p2 = 1e9
for k, v in sz.items():
    if v <= 100000:
        p1 += v
    if v >= need_free:
        p2 = min(p2, v)
print(p1)
print(p2)
