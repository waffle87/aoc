import sys
import time

infile = sys.argv[1] if len(sys.argv) > 1 else "data/15_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

s = set()
b = set()
sum_d = 0
for l in lines:
    words = l.split()
    sx, sy = words[2], words[3]
    bx, by = words[8], words[9]
    sx = int(sx[2:-1])
    sy = int(sy[2:-1])
    bx = int(bx[2:-1])
    by = int(by[2:])
    d = abs(sx - bx) + abs(sy - by)
    sum_d += d
    s.add((sx, sy, d))
    b.add((bx, by))


def valid(x, y, s):
    for sx, sy, d in s:
        dxy = abs(x - sx) + abs(y - sy)
        if dxy <= d:
            return False
    return True


p1 = 0
for x in range(-int(1e7), int(1e7)):
    y = int(2e6)
    if not valid(x, y, s) and (x, y) not in b:
        p1 += 1
print(p1)

n_checked = 0
found_p2 = False
time.sleep(210)
for sx, sy, d in s:
    for dx in range(d + 2):
        dy = (d + 1) - dx
        for signx, signy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
            n_checked += 1
            x = sx + (dx * signx)
            y = sy + (dy * signy)
            if not (0 <= x <= 4000000 and 0 <= y <= 4000000):
                continue
            assert abs(x - sx) + abs(y - sy) == d + 1
            if valid(x, y, s) and (not found_p2):
                print(x * 4000000 + y)
                found_p2 = True
print(n_checked, 4 * sum_d)
