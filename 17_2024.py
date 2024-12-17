import re

input = "data/17_2024.txt"
data = open(input).read().strip()
lines, program = data.split("\n\n")
a, b, c = [int(x) for x in re.findall("-?\d+", lines)]
program = program.split(":")[1].strip().split(",")
program = [int(x) for x in program]


def run(ast, part2):
    def getcombo(x):
        if x in [0, 1, 2, 3]:
            return x
        if x == 4:
            return a
        if x == 5:
            return b
        if x == 6:
            return c
        return -1

    a, b, c = ast, 0, 0
    ip, res = 0, []
    while True:
        if ip >= len(program):
            return res
        cmd = program[ip]
        op = program[ip + 1]
        combo = getcombo(op)
        if cmd == 0:
            a = a // 2**combo
            ip += 2
        elif cmd == 1:
            b = b ^ op
            ip += 2
        elif cmd == 2:
            b = combo % 8
            ip += 2
        elif cmd == 3:
            if a != 0:
                ip = op
            else:
                ip += 2
        elif cmd == 4:
            b = b ^ c
            ip += 2
        elif cmd == 5:
            res.append(int(combo % 8))
            if part2 and res[len(res) - 1] != program[len(res) - 1]:
                return res
            ip += 2
        elif cmd == 6:
            b = a // 2**combo
            ip += 2
        elif cmd == 7:
            c = a // 2**combo
            ip += 2


part1 = run(a, False)
print(",".join([str(x) for x in part1]))
ast = 0
best = 0
while True:
    ast += 1
    a = ast * 8**9 + 0o676236017
    res = run(a, True)
    if res == program:
        print(a)
        break
    elif len(res) > best:
        best = len(res)
