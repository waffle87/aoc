import sys

data = sys.argv[1] if len(sys.argv) > 1 else "../day7data.txt"
X = [int(x) for x in open(data).read().strip().split(",")]

X.sort()
T = X[len(X) // 2]
ans = 0


def C2(d):
    return d * (d + 1) / 2


best = 1e9
for med in range(2000):
    score = 0
    for x in X:
        d = abs(x - med)
        score += C2(d)
    if score < best:
        best = score
print(best)
