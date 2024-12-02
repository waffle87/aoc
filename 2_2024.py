input = "data/2_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
p1, p2 = 0, 0


def is_good(xs):
    inc_dec = xs == sorted(xs) or xs == sorted(xs, reverse=True)
    ok = True
    for i in range(len(xs) - 1):
        diff = abs(xs[i] - xs[i + 1])
        if not 1 <= diff <= 3:
            ok = False
    return inc_dec and ok


for i in lines:
    xs1 = list(map(int, i.split()))
    if is_good(xs1):
        p1 += 1
    good = False
    for j in range(len(xs1)):
        xs = xs1[:j] + xs1[j + 1 :]
        if is_good(xs):
            good = True
    if good:
        p2 += 1

print(p1)
print(p2)
