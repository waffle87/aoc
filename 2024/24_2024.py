input = "data/24_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
wires, ops = {}, []
highest_z = "z00"


def process(op, op1, op2):
    if op == "AND":
        return op1 & op2
    elif op == "OR":
        return op1 | op2
    elif op == "XOR":
        return op1 ^ op2


for i in lines:
    if ":" in i:
        wire, value = i.split(": ")
        wires[wire] = int(value)
    elif "->" in i:
        op1, op, op2, _, res = i.split(" ")
        ops.append((op1, op, op2, res))
        if res[0] == "z" and int(res[1:]) > int(highest_z[1:]):
            highest_z = res

wrong = set()
for op1, op, op2, res in ops:
    if res[0] == "z" and op != "XOR" and res != highest_z:
        wrong.add(res)
    if (
        op == "XOR"
        and res[0] not in ["x", "y", "z"]
        and op1[0] not in ["x", "y", "z"]
        and op2[0] not in ["x", "y", "z"]
    ):
        wrong.add(res)
    if op == "AND" and "x00" not in [op1, op2]:
        for subop1, subop, subop2, subres in ops:
            if (res == subop1 or res == subop2) and subop != "OR":
                wrong.add(res)
    if op == "XOR":
        for subop1, subop, subop2, subres in ops:
            if (res == subop1 or res == subop2) and subop == "OR":
                wrong.add(res)

while len(ops):
    op1, op, op2, res = ops.pop(0)
    if op1 in wires and op2 in wires:
        wires[res] = process(op, wires[op1], wires[op2])
    else:
        ops.append((op1, op, op2, res))

bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
print(int("".join(bits), 2))
print(",".join(sorted(wrong)))
