from re import match
import sys

input = "data/3_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
p1, p2, enabled = 0, 0, True

sys.setrecursionlimit(10**6)
for i in range(len(data)):
    if data[i:].startswith("do()"):
        enabled = True
    if data[i:].startswith("don't()"):
        enabled = False
    instr = match(r"mul\((\d{1,3}),(\d{1,3})\)", data[i:])
    if instr is not None:
        x, y = int(instr.group(1)), int(instr.group(2))
        p1 += x * y
        if enabled:
            p2 += x * y

print(p1)
print(p2)
