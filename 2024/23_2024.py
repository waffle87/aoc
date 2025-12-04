from collections import defaultdict
import random

input = "data/23_2024.txt"
data = open(input).read().strip()
dic = defaultdict(set)
for line in data.split("\n"):
    (
        a,
        b,
    ) = line.split("-")
    dic[a].add(b)
    dic[b].add(a)
xs, p1 = sorted(dic.keys()), 0
for i, a in enumerate(xs):
    for j in range(i + 1, len(xs)):
        for k in range(j + 1, len(xs)):
            b = xs[j]
            c = xs[k]
            if a in dic[b] and a in dic[c] and b in dic[c]:
                if a.startswith("t") or b.startswith("t") or c.startswith("t"):
                    p1 += 1
print(p1)
best = None
for t in range(1000):
    random.shuffle(xs)
    clique = []
    for x in xs:
        ok = True
        for y in clique:
            if x not in dic[y]:
                ok = False
        if ok:
            clique.append(x)
    if best is None or len(clique) > len(best):
        best = clique
print(",".join(sorted(best)))
