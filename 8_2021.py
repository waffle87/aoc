import sys
import itertools
from collections import defaultdict, Counter

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


def findPermSlow(before):
    for perm in itertools.permutations(list(range(8))):
        ok = True
        D = {}
        for i in range(8):
            D[chr(ord("a") + i)] = chr(ord("a") + perm[i])
        for w in before:
            wPerm = ""
            for c in w:
                wPerm += D[c]
            wPerm = "".join(sorted(wPerm))
            if wPerm not in digits.values():
                ok = False
        if ok:
            return D


def findPerm(before):
    A = {}
    for w in before:
        if len(w) == 2:
            cf = w
    assert len(cf) == 2, cf
    for w in before:
        if len(w) == 6 and (cf[0] in w) != (cf[1] in w):
            if cf[0] in w:
                A[cf[0]] = "f"
                A[cf[1]] = "c"
            else:
                A[cf[1]] = "f"
                A[cf[0]] = "c"
    assert len(A) == 2, f"A = {A} cf = {cf} {before}"
    for w in before:
        if len(w) == 3:
            for c in w:
                if c not in cf:
                    A[c] = "a"
    assert len(A) == 3, A
    for w in before:
        if len(w) == 4:
            bd = ""
            for c in w:
                if c not in cf:
                    bd += c
    assert len(bd) == 2, bd
    for w in before:
        if len(w) == 6 and (bd[0] in w) != (bd[1] in w):
            if bd[0] in w:
                A[bd[0]] = "b"
                A[bd[1]] = "d"
            else:
                A[bd[1]] = "b"
                A[bd[0]] = "d"
    assert len(A) == 5, A
    eg = ""
    for c in ["a", "b", "c", "d", "e", "f", "g"]:
        if c not in A:
            eg += c
    assert len(eg) == 2, eg
    for w in before:
        if len(w) == 6 and (eg[0] in w) != (eg[1] in w):
            if eg[0] in w:
                A[eg[0]] = "g"
                A[eg[1]] = "e"
            else:
                A[eg[1]] = "g"
                A[eg[0]] = "e"
    assert len(A) == 7, A
    return A


p1 = 0
ans = 0
data = sys.argv[1] if len(sys.argv) > 1 else "../day8data.txt"
for line in open(data):
    before, after = line.split("|")
    before = before.split()
    after = after.split()
    D = findPerm(before)
    ret = ""
    for w in after:
        wPerm = ""
        for c in w:
            wPerm += D[c]
        wPerm = "".join(sorted(wPerm))
        d = [k for k, v in digits.items() if v == wPerm]
        assert len(d) == 1
        if d[0] in [1, 4, 7, 8]:
            p1 += 1
        ret += str(d[0])
    ans += int(ret)

print(p1)
print(ans)
