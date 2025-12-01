input = "data/1_2025.txt"
data = open(input).read().strip()
lines = data.splitlines()
pos = 50
p1, p2 = 0, 0

for line in lines:
    dir, cnt = line[0], int(line[1:])
    for _ in range(cnt):
        if dir == "L":
            pos = (pos - 1 + 100) % 100
        else:
            pos = (pos + 1) % 100
        if pos == 0:
            p2 += 1
    if pos == 0:
        p1 += 1

print(p1)
print(p2)
