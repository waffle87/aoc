from collections import defaultdict

input = "data/8_2024.txt"
data = open(input).read().strip()
line = data.split("\n")
row, col = len(line), len(line[0])
a1, a2, dic = set(), set(), defaultdict(list)


for r in range(row):
    for c in range(col):
        if line[r][c] != ".":
            dic[line[r][c]].append((r, c))


for r in range(row):
    for c in range(col):
        for k, vs in dic.items():
            for r1, c1 in vs:
                for r2, c2 in vs:
                    if (r1, c1) != (r2, c2):
                        d1 = abs(r - r1) + abs(c - c1)
                        d2 = abs(r - r2) + abs(c - c2)
                        dr1 = r - r1
                        dr2 = r - r2
                        dc1 = c - c1
                        dc2 = c - c2
                        if (
                            (d1 == 2 * d2 or d1 * 2 == d2)
                            and 0 <= r < row
                            and 0 <= c < col
                            and (dr1 * dc2 == dc1 * dr2)
                        ):
                            a1.add((r, c))
                        if 0 <= r < row and 0 <= c < col and (dr1 * dc2 == dc1 * dr2):
                            a2.add((r, c))


p1 = len(a1)
p2 = len(a2)
print(p1)
print(p2)
