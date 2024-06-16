import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "data/14_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

r = set()
for l in lines:
    prev = None
    for p in l.split("->"):
        x, y = p.split(",")
        x, y = int(x), int(y)
        if prev is not None:
            dx = x - prev[0]
            dy = y - prev[1]
            len_ = max(abs(dx), abs(dy))
            for i in range(len_ + 1):
                xx = prev[0] + i * (1 if dx > 0 else (-1 if dx < 0 else 0))
                yy = prev[1] + i * (1 if dy > 0 else (-1 if dy < 0 else 0))
                r.add((xx, yy))
        prev = (x, y)

floor = 2 + max(i[1] for i in r)
low_x = min(i[0] for i in r) - 2000
high_x = max(i[0] for i in r) + 2000
for x in range(low_x, high_x):
    r.add((x, floor))

did_p1 = False
for t in range(1000000):
    rock = (500, 0)
    while True:
        if rock[1] + 1 >= floor and (not did_p1):
            did_p1 = True
            print(t)
        if (rock[0], rock[1] + 1) not in r:
            rock = (rock[0], rock[1] + 1)
        elif (rock[0] - 1, rock[1] + 1) not in r:
            rock = (rock[0] - 1, rock[1] + 1)
        elif (rock[0] + 1, rock[1] + 1) not in r:
            rock = (rock[0] + 1, rock[1] + 1)
        else:
            break
    if rock == (500, 0):
        print(t + 1)
        break
    r.add(rock)
