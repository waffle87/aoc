import z3

input = open("data/10_2025.txt")
data = input.read().splitlines()
p1, p2 = 0, 0

for i in data:
    words = i.split()
    goal = words[0]
    goal = goal[1:-1]
    goal_n = 0
    for j, k in enumerate(goal):
        if k == "#":
            goal_n += 2**j

    buttons = words[1:-1]
    b, ns = [], []

    for j in buttons:
        n = [int(x) for x in j[1:-1].split(",")]
        button_n = sum(2**x for x in n)
        b.append(button_n)
        ns.append(n)

    score = len(buttons)
    for j in range(2 ** len(buttons)):
        a_n, a_score = 0, 0
        for k in range(len(buttons)):
            if ((j >> k) % 2) == 1:
                a_n ^= b[k]
                a_score += 1
        if a_n == goal_n:
            score = min(score, a_score)
    p1 += score
    joltage = words[-1]
    joltage_ns = [int(x) for x in joltage[1:-1].split(",")]
    v = []
    for j in range(len(buttons)):
        v.append(z3.Int(f"b{j}"))
    eq = []
    for j in range(len(joltage_ns)):
        terms = []
        for k in range(len(buttons)):
            if j in ns[k]:
                terms.append(v[k])
        eq_n = sum(terms) == joltage_ns[j]
        eq.append(eq_n)
    o = z3.Optimize()
    o.minimize(sum(v))
    for j in eq:
        o.add(j)
    for j in v:
        o.add(j >= 0)
    assert o.check()
    m = o.model()
    for j in m.decls():
        p2 += m[j].as_long()

print(p1)
print(p2)
