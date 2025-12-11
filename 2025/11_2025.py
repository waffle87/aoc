from functools import cache

input = open("data/11_2025.txt").read()
data = input.splitlines()
e = {}

for i in data:
    x, y = i.split(":")
    y = y.split()
    e[x] = y


@cache
def part1(x):
    if x == "out":
        return 1
    else:
        return sum(part1(i) for i in e[x])


@cache
def part2(x, vis_dac, vis_fft):
    if x == "out":
        return 1 if vis_dac and vis_fft else 0
    else:
        res = 0
        for i in e[x]:
            new_vis_dac = vis_dac or i == "dac"
            new_vis_fft = vis_fft or i == "fft"
            res += part2(i, new_vis_dac, new_vis_fft)
        return res


print(part1("you"))
print(part2("svr", False, False))
