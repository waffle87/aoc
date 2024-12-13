infile = "data/13_2024.txt"
data = open(infile).read().strip()
lines = data.split("\n\n")
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
p1 = 0
p2 = 0


def solve(ax, ay, bx, by, px, py, parj):
    p2, best = 10000000000000 if parj else 0, None
    for i in range(600):
        for j in range(600):
            cost = 3 * i + j
            dx = ax * i + bx * j
            dy = ay * i + by * j
            if dx == dy and dx > 0:
                score = dx / cost
                if best is None or score < best[0]:
                    best = (score, i, j, cost, dx)
    if best is None:
        return 0
    curr, i, j, cost, dx = best
    amt = (p2 - 40000) // dx
    dp = {}

    def f(x, y):
        if (x, y) in dp:
            return dp[(x, y)]
        if x == 0 and y == 0:
            return 0
        if x < 0:
            return 10**20
        if y < 0:
            return 10**20
        res = min(3 + f(x - ax, y - ay), 1 + f(x - bx, y - by))
        dp[(x, y)] = res
        return res

    res = f(px + p2 - amt * dx, py + p2 - amt * dx)
    if res < 10**15:
        return res + amt * cost
    else:
        return 0


for i, j in enumerate(lines):
    a, b, prize = j.split("\n")
    aw = a.split()
    ax = int(aw[2].split("+")[1].split(",")[0])
    ay = int(aw[3].split("+")[1].split(",")[0])
    bw = b.split()
    bx = int(bw[2].split("+")[1].split(",")[0])
    by = int(bw[3].split("+")[1].split(",")[0])
    pw = prize.split()
    px = int(pw[1].split("=")[1].split(",")[0])
    py = int(pw[2].split("=")[1])
    p1 += solve(ax, ay, bx, by, px, py, False)
    p2 += solve(ax, ay, bx, by, px, py, True)


print(p1)
print(p2)
