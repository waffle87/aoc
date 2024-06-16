import sys
from typing import List
from dataclasses import dataclass
import re
from copy import deepcopy
from math import gcd
from collections import defaultdict, Counter, deque
import heapq


"""
square. we start on the square centred at (0, 0). each square corresponds to the
grid point in its centre. we are tracing out some shape following the
instructions; instead of cutting out whole squares, imagine drawing a line
through the corresponding grid points

pick's theorem: suppose we have a polygon with the integer coordinates with area
A, B integer points along its boundary, and I integer points strictly within.
then A = I + (B / 2) - 1

the solution to the problem is just I + B, the number of grid points / squares
in the same, plus the number of squares / points on the inside of the same.
rearranging, pick's theorem tells us I = A (B / 2) + 1. so I + B = A + (B / 2)
+ 1. B is just the perimeter minus the sum of N across all commands. (note, each
command actually covers N + 1 squares, but the ending square of each command is
also covered by the starting square of the next command. so summing N gets the
correct number of squares in the path). we can compute the area A in two
different ways:
- the shoelace formula: A = (sum X[i] * Y[i + 1] - X[i + 1] * Y[i]) // 2
- green's theorem: A = sum y * dx = sum x * dy
"""


@dataclass
class Instruction:
    d: str
    n: int


def parse_input(input_: str, part2: bool) -> List[Instruction]:
    ans = []
    for line in input_.split("\n"):
        d, n, hex_ = line.split()
        if not part2:
            ans.append(Instruction(d, int(n)))
        else:
            hex_ = hex_[1:-1]
            d = {0: "R", 1: "D", 2: "L", 3: "U"}[int(hex_[-1])]
            n = int(hex_[1:-1], 16)
            ans.append(Instruction(d, n))
    return ans


def area_shoelace(cmds: List[Instruction]) -> int:
    V = []
    pos = (0, 0)
    for cmd in cmds:
        d, n = cmd.d, cmd.n
        if d == "R":
            pos = (pos[0] + n, pos[1])
        elif d == "D":
            pos = (pos[0], pos[1] - n)
        elif d == "L":
            pos = (pos[0] - n, pos[1])
        elif d == "U":
            pos = (pos[0], pos[1] + n)
        V.append(pos)
    area = 0
    for i in range(len(V)):
        area -= V[i][0] * V[(i + 1) % len(V)][1]
        area += V[i][1] * V[(i + 1) % len(V)][0]
    area //= 2
    return area


def area_green(cmds: List[Instruction]) -> int:
    area = 0
    y = 0
    for cmd in cmds:
        if cmd.d == "R":
            area += y * cmd.n
        elif cmd.d == "L":
            area -= y * cmd.n
        elif cmd.d == "U":
            y += cmd.n
        elif cmd.d == "D":
            y -= cmd.n
    return area


D = open(sys.argv[1]).read().strip()
for part2 in [False, True]:
    cmds = parse_input(D, part2)
    perimeter = 0
    for cmd in cmds:
        perimeter += cmd.n
    area1 = area_shoelace(cmds)
    area2 = area_green(cmds)
    assert area1 == area2, f"shoelace={area1} green={area2}"
    ans = area1 + (perimeter // 2) + 1
    print(ans)
