import sys
from collections import defaultdict, Counter, deque

SCORES = []
ans = 0
data = sys.argv[1] if len(sys.argv) > 1 else "day10data.txt"
for line in open(data):
    bad = False
    S = deque()
    for c in line.strip():
        if c in ["(", "[", "{", "<"]:
            S.append(c)
        elif c == ")":
            if S[-1] != "(":
                ans += 3
                bad = True
                break
            else:
                S.pop()
        elif c == "]":
            if S[-1] != "[":
                ans += 57
                bad = True
                break
            else:
                S.pop()
        elif c == "}":
            if S[-1] != "{":
                ans += 1197
                bad = True
                break
            else:
                S.pop()
        elif c == ">":
            if S[-1] != "<":
                ans += 25137
                bad = True
                break
            else:
                S.pop()
    if not bad:
        score = 0
        P = {"(": 1, "[": 2, "{": 3, "<": 4}
        for c in reversed(S):
            score = score * 5 + P[c]
        SCORES.append(score)
print(ans)
SCORES.sort()
print(SCORES[len(SCORES) // 2])
