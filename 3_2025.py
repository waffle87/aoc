def fun(line, i, used):
    if i == len(line) and used == 12:
        return 0
    if i == len(line):
        return -(10**20)
    key = (i, used)
    if key in dp:
        return dp[key]
    res = fun(line, i + 1, used)
    if used < 12:
        res = max(res, 10 ** (11 - used) * int(line[i]) + fun(line, i + 1, used + 1))
    dp[key] = res
    return res


input = "data/3_2025.txt"
data = open(input).read().strip()
lines = data.splitlines()

p1, p2 = 0, 0
for line in lines:
    dp, best = {}, None
    p2 += fun(line, 0, 0)
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            score = int(line[i] + line[j])
            if best is None or score > best:
                best = score
    p1 += best

print(p1)
print(p2)
