input = "data/25_2024.txt"
data = open(input).read().strip()
shapes = data.split("\n\n")
keys, locks = [], []
for shape in shapes:
    G = shape.split("\n")
    rows = len(G)
    cols = len(G[0])
    G = [[G[r][c] for c in range(cols)] for r in range(rows)]
    is_key = True
    for c in range(cols):
        if G[0][c] == "#":
            is_key = False
    if is_key:
        keys.append(shape)
    else:
        locks.append(shape)


def fits(key, lock):
    rows = len(key)
    assert rows == len(lock)
    cols = len(key[0])
    assert cols == len(lock[0])
    for r in range(rows):
        for c in range(cols):
            if key[r][c] == "#" and lock[r][c] == "#":
                return False
    return True


ans = 0
for key in keys:
    for lock in locks:
        if fits(key, lock):
            ans += 1
print(ans)
