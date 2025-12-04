input = "data/22_2024.txt"
data = open(input).read().strip()


def mix(x, y):
    return x ^ y


def prune(x):
    return x % 16777216


def prices(x):
    res = [x]
    for _ in range(2000):
        x = prune(mix(x, 64 * x))
        x = prune(mix(x, x // 32))
        x = prune(mix(x, x * 2048))
        res.append(x)
    return res


def changes(p):
    return [p[i + 1] - p[i] for i in range(len(p) - 1)]


def getscores(p, c):
    res = {}
    for i in range(len(c) - 3):
        pattern = (c[i], c[i + 1], c[i + 2], c[i + 3])
        if pattern not in res:
            res[pattern] = p[i + 4]
    return res


p1, score = 0, {}
for line in data.split("\n"):
    p = prices(int(line))
    p1 += p[-1]
    p = [x % 10 for x in p]
    c = changes(p)
    s = getscores(p, c)
    for k, v in s.items():
        if k not in score:
            score[k] = v
        else:
            score[k] += v
print(p1)
print(max(score.values()))
