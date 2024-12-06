infile = "data/6_2024.txt"
data = open(infile).read().strip()
lines = data.split("\n")
p1, p2 = 0, 0
rows = len(lines)
cols = len(lines[0])


for r in range(rows):
    for c in range(cols):
        if lines[r][c] == "^":
            sr, sc = r, c
for o_r in range(rows):
    for o_c in range(cols):
        r, c, d = sr, sc, 0
        vis, vis_rc = set(), set()
        while True:
            if (r, c, d) in vis:
                p2 += 1
                break
            vis.add((r, c, d))
            vis_rc.add((r, c))
            dr, dc = [(-1, 0), (0, 1), (1, 0), (0, -1)][d]
            rr = r + dr
            cc = c + dc
            if not (0 <= rr < rows and 0 <= cc < cols):
                if lines[o_r][o_c] == "#":
                    p1 = len(vis_rc)
                break
            if lines[rr][cc] == "#" or rr == o_r and cc == o_c:
                d = (d + 1) % 4
            else:
                r = rr
                c = cc

print(p1)
print(p2)
