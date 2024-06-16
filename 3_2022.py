def score(c):
    if "a" <= c <= "z":
        return ord(c) - ord("a") + 1
    else:
        return ord(c) - ord("A") + 27


p1 = 0
for line in open("3_2022.txt"):
    x = line.strip()
    assert len(x) % 2 == 0
    y, z = x[: len(x) // 2], x[len(x) // 2 :]
    for c in y:
        if c in z:
            p1 += score(c)
            break
print(p1)

p2 = 0
i = [line for line in open("3_2022.txt")]
j = 0
while j < len(i):
    for c in i[j]:
        if c in i[j + 1] and c in i[j + 2]:
            p2 += score(c)
            break
    j += 3
print(p2)
