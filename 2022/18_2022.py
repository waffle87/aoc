import sys
from collections import deque

infile = sys.argv[1] if len(sys.argv) > 1 else "data/18_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

P = set()
out = set()
in_ = set()
for l in lines:
    x, y, z = l.split(",")
    x, y, z = int(x), int(y), int(z)
    P.add((x, y, z))


def reaches_outside(x, y, z, part):
    if (x, y, z) in out:
        return True
    if (x, y, z) in in_:
        return False
    seen = set()
    q = deque([(x, y, z)])
    while q:
        x, y, z = q.popleft()
        if (x, y, z) in P:
            continue
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if len(seen) > (5000 if part == 2 else 0):
            for p in seen:
                out.add(p)
            return True
        q.append((x + 1, y, z))
        q.append((x - 1, y, z))
        q.append((x, y + 1, z))
        q.append((x, y - 1, z))
        q.append((x, y, z + 1))
        q.append((x, y, z - 1))
    for p in seen:
        in_.add(p)
    return False


def solve(part):
    out.clear()
    in_.clear()
    ans = 0
    for x, y, z in P:
        if reaches_outside(x + 1, y, z, part):
            ans += 1
        if reaches_outside(x - 1, y, z, part):
            ans += 1
        if reaches_outside(x, y + 1, z, part):
            ans += 1
        if reaches_outside(x, y - 1, z, part):
            ans += 1
        if reaches_outside(x, y, z + 1, part):
            ans += 1
        if reaches_outside(x, y, z - 1, part):
            ans += 1
    return ans


print(solve(1))
print(solve(2))
