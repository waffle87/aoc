import sys
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv) > 1 else "data/11_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]

m = []
op = []
div = []
true = []
false = []
for monkey in data.split("\n\n"):
    id_, items, op_, test, t, f = monkey.split("\n")
    m.append([int(i) for i in items.split(":")[1].split(",")])
    words = op_.split()
    op_ = "".join(words[-3:])
    # last 3 words of input are a valid python function of the single variable 'old'
    op.append(lambda old, op_=op_: eval(op_))
    div.append(int(test.split()[-1]))
    true.append(int(t.split()[-1]))
    false.append(int(f.split()[-1]))

start = deepcopy(m)

# want to know for each item if it's divisible by 23, 19, 13, 17
# we can check using modulo eg. val % 17
# x + a is divisible by 23 if (x % 23) + a is divisible by 23
# x * a is divisible by 23 if (x % 23) * a is divisible by 23
# now keep track of number modulo 23 * 19 * 13 * 17
lcm = 1
for x in div:
    lcm = lcm * x  # math.gcd(lcm, x)
# print(len(str(lcm)))

for part in [1, 2]:
    c = [0 for _ in range(len(m))]
    m = deepcopy(start)
    for t in range(20 if part == 1 else 10000):
        for i in range(len(m)):
            for item in m[i]:
                # print(i, item)
                c[i] += 1
                item = op[i](item)
                if part == 2:
                    item %= lcm
                # print(i, item)
                if part == 1:
                    item = item // 3
                # print(i, item, item % div[i], true[i], false[i])
                if item % div[i] == 0:
                    # print(f'item {item} thrown to {true[i]}')
                    m[true[i]].append(item)
                else:
                    # print(f'item {item} thrown to {false[i]}')
                    m[false[i]].append(item)
            m[i] = []
    print(sorted(c)[-1] * sorted(c)[-2])
