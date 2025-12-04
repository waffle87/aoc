import sys
from copy import deepcopy

infile = sys.argv[1] if len(sys.argv) > 1 else "5_2022.txt"
data = open(infile).read()
lines = [x for x in data.split("\n")]

i = []
cmds = []
for line in lines:
    if line == "":
        break
    sz = (len(line) + 1) // 4
    while len(i) < sz:
        i.append([])
    for j in range(len(i)):
        ch = line[1 + 4 * j]
        if ch != " " and "A" <= ch <= "Z":
            i[j].append(ch)

p1 = deepcopy(i)
p2 = deepcopy(i)
found = False
for cmd in lines:
    if cmd == "":
        found = True
        continue
    if not found:
        continue
    words = cmd.split()
    qty = int(words[1])
    frm = int(words[3]) - 1
    too = int(words[5]) - 1
    for ST, do_rev in [(p1, True), (p2, False)]:
        MOVE = ST[frm][:qty]
        ST[frm] = ST[frm][qty:]
        ST[too] = (list(reversed(MOVE)) if do_rev else MOVE) + ST[too]
print("".join([s[0] for s in p1 if len(s) > 0]))
print("".join([s[0] for s in p2 if len(s) > 0]))
