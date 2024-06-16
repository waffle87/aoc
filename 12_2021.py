import sys
from collections import defaultdict, deque

data = sys.argv[1] if len(sys.argv) > 1 else "day12data.txt"
E = defaultdict(list)
for line in open(data):
    a, b = line.strip().split("-")
    E[a].append(b)
    E[b].append(a)


def solve(p1):
    start = ("start", set(["start"]), None)
    ans = 0
    Q = deque([start])
    while Q:
        pos, small, twice = Q.popleft()
        if pos == "end":
            ans += 1
            continue
        for y in E[pos]:
            if y not in small:
                newSmall = set(small)
                if y.lower() == y:
                    newSmall.add(y)
                Q.append((y, newSmall, twice))
            elif y in small and twice is None and y not in ["start", "end"] and not p1:
                Q.append((y, small, y))
    return ans


print(solve(p1=True))
print(solve(p1=False))
