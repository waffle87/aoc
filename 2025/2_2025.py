def invalid(s, p2):
    s = str(s)
    for k in range(2, len(s) + 1 if p2 else 3):
        if len(s) % k == 0:
            valid = True
            n, i = len(s) // k, 0
            while i < len(s):
                if s[i : i + n] != s[:n]:
                    valid = False
                i += n
            if valid:
                return True
    return False


input = "data/2_2025.txt"
data = open(input).read().split(",")
p1, p2 = 0, 0

for i in data:
    first, last = i.split("-")
    first = int(first)
    last = int(last)
    for j in range(first, last + 1):
        if invalid(j, False):
            p1 += j
        if invalid(j, True):
            p2 += j

print(p1)
print(p2)
