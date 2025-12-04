from collections import deque

input = "data/9_2024.txt"
data = open(input).read().strip()


def solve(part2):
    q, space = deque([]), deque([])
    id, pos, final = 0, 0, []
    for i, c in enumerate(data):
        if i % 2 == 0:
            if part2:
                q.append((pos, int(c), id))
            for i in range(int(c)):
                final.append(id)
                if not part2:
                    q.append((pos, 1, id))
                pos += 1
            id += 1
        else:
            space.append((pos, int(c)))
            for i in range(int(c)):
                final.append(None)
                pos += 1
    for pos, size, id in reversed(q):
        for space_i, (space_pos, space_size) in enumerate(space):
            if space_pos < pos and size <= space_size:
                for i in range(size):
                    assert final[pos + i] == id, f"{final[pos+i]=}"
                    final[pos + i] = None
                    final[space_pos + i] = id
                space[space_i] = (space_pos + size, space_size - size)
                break
    res = 0
    for i, c in enumerate(final):
        if c is not None:
            res += i * c
    return res


p1 = solve(False)
p2 = solve(True)

print(p1)
print(p2)
