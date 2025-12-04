import sys
from pyperclip import copy

input = "data/4_2024.txt"
data = open(input).read().strip()
lines = data.split("\n")
sys.setrecursionlimit(10**6)
p1, p2 = 0, 0
rows = len(lines)
cols = len(lines[0])


for r in range(rows):
    for c in range(cols):
        if (
            c + 3 < cols
            and lines[r][c] == "X"
            and lines[r][c + 1] == "M"
            and lines[r][c + 2] == "A"
            and lines[r][c + 3] == "S"
        ):
            p1 += 1
        if (
            r + 3 < rows
            and lines[r][c] == "X"
            and lines[r + 1][c] == "M"
            and lines[r + 2][c] == "A"
            and lines[r + 3][c] == "S"
        ):
            p1 += 1
        if (
            r + 3 < rows
            and c + 3 < cols
            and lines[r][c] == "X"
            and lines[r + 1][c + 1] == "M"
            and lines[r + 2][c + 2] == "A"
            and lines[r + 3][c + 3] == "S"
        ):
            p1 += 1
        if (
            c + 3 < cols
            and lines[r][c] == "S"
            and lines[r][c + 1] == "A"
            and lines[r][c + 2] == "M"
            and lines[r][c + 3] == "X"
        ):
            p1 += 1
        if (
            r + 3 < rows
            and lines[r][c] == "S"
            and lines[r + 1][c] == "A"
            and lines[r + 2][c] == "M"
            and lines[r + 3][c] == "X"
        ):
            p1 += 1
        if (
            r + 3 < rows
            and c + 3 < cols
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 3][c + 3] == "X"
        ):
            p1 += 1
        if (
            r - 3 >= 0
            and c + 3 < cols
            and lines[r][c] == "S"
            and lines[r - 1][c + 1] == "A"
            and lines[r - 2][c + 2] == "M"
            and lines[r - 3][c + 3] == "X"
        ):
            p1 += 1
        if (
            r - 3 >= 0
            and c + 3 < cols
            and lines[r][c] == "X"
            and lines[r - 1][c + 1] == "M"
            and lines[r - 2][c + 2] == "A"
            and lines[r - 3][c + 3] == "S"
        ):
            p1 += 1
        if (
            r + 2 < rows
            and c + 2 < cols
            and lines[r][c] == "M"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "S"
            and lines[r + 2][c] == "M"
            and lines[r][c + 2] == "S"
        ):
            p2 += 1
        if (
            r + 2 < rows
            and c + 2 < cols
            and lines[r][c] == "M"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "S"
            and lines[r + 2][c] == "S"
            and lines[r][c + 2] == "M"
        ):
            p2 += 1
        if (
            r + 2 < rows
            and c + 2 < cols
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 2][c] == "M"
            and lines[r][c + 2] == "S"
        ):
            p2 += 1
        if (
            r + 2 < rows
            and c + 2 < cols
            and lines[r][c] == "S"
            and lines[r + 1][c + 1] == "A"
            and lines[r + 2][c + 2] == "M"
            and lines[r + 2][c] == "S"
            and lines[r][c + 2] == "M"
        ):
            p2 += 1


def solve(s):
    print(s)
    copy(s)


solve(p1)
solve(p2)
