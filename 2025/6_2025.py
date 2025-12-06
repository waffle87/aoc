input = open("data/6_2025.txt").read()
grid = [list(i) for i in input.splitlines()]
r, c = len(grid), len(grid[0])
p1, p2, start = 0, 0, 0

for cc in range(c + 1):
    blank = True
    if cc < c:
        for i in range(r):
            if grid[i][cc] != " ":
                blank = False
    if blank:
        op = grid[r - 1][start]
        assert op in ["+", "*"], op
        p1_score = 0 if op == "+" else 1
        for i in range(r - 1):
            p1_n = 0
            for j in range(start, cc):
                if grid[i][j] != " ":
                    p1_n = p1_n * 10 + int(grid[i][j])
            if op == "*":
                p1_score *= p1_n
            else:
                p1_score += p1_n
        p1 += p1_score

        p2_score = 0 if op == "+" else 1
        for i in range(cc - 1, start - 1, -1):
            n = 0
            for j in range(r - 1):
                if grid[j][i] != " ":
                    n = n * 10 + int(grid[j][i])
            if op == "+":
                p2_score += n
            else:
                p2_score *= n
        p2 += p2_score
        start = cc + 1

print(p1)
print(p2)
