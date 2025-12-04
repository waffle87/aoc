from collections import deque

input = "data/15_2024.txt"
data = open(input).read().strip()
lines, instrs = data.split("\n\n")
lines = lines.split("\n")


def solve(lines, part2):
    rows = len(lines)
    cols = len(lines[0])
    lines = [[lines[r][c] for c in range(cols)] for r in range(rows)]
    if part2:
        big = []
        for r in range(rows):
            row = []
            for c in range(cols):
                if lines[r][c] == "#":
                    row.append("#")
                    row.append("#")
                if lines[r][c] == "O":
                    row.append("[")
                    row.append("]")
                if lines[r][c] == ".":
                    row.append(".")
                    row.append(".")
                if lines[r][c] == "@":
                    row.append("@")
                    row.append(".")
            big.append(row)
        lines = big
        cols *= 2
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] == "@":
                sr, sc = r, c
                lines[r][c] = "."
    r, c = sr, sc
    for inst in instrs:
        if inst == "\n":
            continue
        dr, dc = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}[inst]
        rr, cc = r + dr, c + dc
        if lines[rr][cc] == "#":
            continue
        elif lines[rr][cc] == ".":
            r, c = rr, cc
        elif lines[rr][cc] in ["[", "]", "O"]:
            q = deque([(r, c)])
            vis = set()
            ok = True
            while q:
                rr, cc = q.popleft()
                if (rr, cc) in vis:
                    continue
                vis.add((rr, cc))
                rrr, ccc = rr + dr, cc + dc
                if lines[rrr][ccc] == "#":
                    ok = False
                    break
                if lines[rrr][ccc] == "O":
                    q.append((rrr, ccc))
                if lines[rrr][ccc] == "[":
                    q.append((rrr, ccc))
                    assert lines[rrr][ccc + 1] == "]"
                    q.append((rrr, ccc + 1))
                if lines[rrr][ccc] == "]":
                    q.append((rrr, ccc))
                    assert lines[rrr][ccc - 1] == "["
                    q.append((rrr, ccc - 1))
            if not ok:
                continue
            while len(vis) > 0:
                for rr, cc in sorted(vis):
                    rrr, ccc = rr + dr, cc + dc
                    if (rrr, ccc) not in vis:
                        assert lines[rrr][ccc] == "."
                        lines[rrr][ccc] = lines[rr][cc]
                        lines[rr][cc] = "."
                        vis.remove((rr, cc))
            r = r + dr
            c = c + dc
    res = 0
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] in ["[", "O"]:
                res += 100 * r + c
    return res


print(solve(lines, False))
print(solve(lines, True))
