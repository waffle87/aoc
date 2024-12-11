input = "data/11_2024.txt"
data = open(input).read().strip()
data = [int(x) for x in data.split()]
dp = {}


def solve(x, t):
    if (x, t) in dp:
        return dp[(x, t)]
    if t == 0:
        res = 1
    elif x == 0:
        res = solve(1, t - 1)
    elif len(str(x)) % 2 == 0:
        dstr = str(x)
        left = dstr[: len(dstr) // 2]
        right = dstr[len(dstr) // 2 :]
        left, right = (int(left), int(right))
        res = solve(left, t - 1) + solve(right, t - 1)
    else:
        res = solve(x * 2024, t - 1)
    dp[(x, t)] = res
    return res


def solve_all(t):
    return sum(solve(x, t) for x in data)


print(solve_all(25))
print(solve_all(75))
