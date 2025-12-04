from collections import Counter

input = "data/1_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
left, right, rc = [], [], Counter()

for i in lines:
    l, r = i.split()
    l, r = int(l), int(r)
    left.append(l)
    right.append(r)
    rc[r] += 1

p1 = 0
left, right = sorted(left), sorted(right)
for l, r in zip(left, right):
    p1 += abs(r - l)
print(p1)

p2 = 0
for l in left:
    p2 += l * rc.get(l, 0)
print(p2)
