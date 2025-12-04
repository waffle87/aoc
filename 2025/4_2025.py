input = "data/4_2025.txt"
data = open(input).read()
grid = [list(i) for i in data.splitlines()]

n, m = len(grid), len(grid[0])
p1, p2 = 0, 0
first = True

while True:
    changed = False
    for r in range(n):
        for c in range(m):
            num = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < n and 0 <= cc < m and grid[rr][cc] == "@":
                        num += 1
            if grid[r][c] == "@" and num < 5:
                p1 += 1
                changed = True
                if not first:
                    p2 += 1
                    grid[r][c] = "."
    if first:
        print(p1)
        first = False
    if not changed:
        break

print(p2)
