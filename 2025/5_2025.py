input = open("data/5_2025.txt").read()
ranges, ingredients = input.split("\n\n")
arr = []

for i in ranges.splitlines():
    start, end = i.split("-")
    start = int(start)
    end = int(end)
    arr.append((start, end))

p2, curr = 0, -1
arr = sorted(arr)

for i, j in arr:
    if curr >= i:
        i = curr + 1
    if i <= j:
        p2 += j - i + 1
    curr = max(curr, j)

p1 = 0
for i in ingredients.splitlines():
    i = int(i)
    new = False
    for j, k in arr:
        if j <= i <= k:
            new = True
    if new:
        p1 += 1

print(p1)
print(p2)
