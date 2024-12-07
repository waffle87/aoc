input = "data/7_2024.txt"
data = open(input).read().strip()
p1, p2 = 0, 0


def valid(target, ns, p2):
    if len(ns) == 1:
        return ns[0] == target
    if valid(target, [ns[0] + ns[1]] + ns[2:], p2):
        return True
    if valid(target, [ns[0] * ns[1]] + ns[2:], p2):
        return True
    if p2 and valid(target, [int(str(ns[0]) + str(ns[1]))] + ns[2:], p2):
        return True
    return False


for line in data.strip().split("\n"):
    target, ns = line.strip().split(":")
    target = int(target)
    ns = [int(x) for x in ns.strip().split()]
    if valid(target, ns, p2=False):
        p1 += target
    if valid(target, ns, p2=True):
        p2 += target


print(p1)
print(p2)
