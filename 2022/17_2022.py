import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "data/17_2022.txt"
data = open(infile).read().strip()
lines = [x for x in data.split("\n")]


def get_piece(t, y):
    if t == 0:
        return set([(2, y), (3, y), (4, y), (5, y)])
    elif t == 1:
        return set([(3, y + 2), (2, y + 1), (3, y + 1), (4, y + 1), (3, y)])
    elif t == 2:
        return set([(2, y), (3, y), (4, y), (4, y + 1), (4, y + 2)])
    elif t == 3:
        return set([(2, y), (2, y + 1), (2, y + 2), (2, y + 3)])
    elif t == 4:
        return set([(2, y + 1), (2, y), (3, y + 1), (3, y)])
    else:
        assert False


def move_left(piece):
    if any([x == 0 for (x, y) in piece]):
        return piece
    return set([(x - 1, y) for (x, y) in piece])


def move_right(piece):
    if any([x == 6 for (x, y) in piece]):
        return piece
    return set([(x + 1, y) for (x, y) in piece])


def move_down(piece):
    return set([(x, y - 1) for (x, y) in piece])


def move_up(piece):
    return set([(x, y + 1) for (x, y) in piece])


def show(r):
    max_y = max([y for (x, y) in r])
    for y in range(max_y, 0, -1):
        row = ""
        for x in range(7):
            if (x, y) in r:
                row += "#"
            else:
                row += " "
        print(row)


r = set([(x, 0) for x in range(7)])


def signature(r):
    max_y = max([y for (x, y) in r])
    return frozenset([(x, max_y - y) for (x, y) in r if max_y - y <= 30])


l = 1000000000000
seen = {}
top = 0
i = 0
t = 0
added = 0
while t < l:
    piece = get_piece(t % 5, top + 4)
    while True:
        if data[i] == "<":
            piece = move_left(piece)
            if piece & r:
                piece = move_right(piece)
        else:
            piece = move_right(piece)
            if piece & r:
                piece = move_left(piece)
        i = (i + 1) % len(data)
        piece = move_down(piece)
        if piece & r:
            piece = move_up(piece)
            r |= piece
            top = max([y for (x, y) in r])
            sr = (i, t % 5, signature(r))
            if sr in seen and t >= 2022:
                (old_t, old_y) = seen[sr]
                dy = top - old_y
                dt = t - old_t
                amt = (l - t) // dt
                added += amt * dy
                t += amt * dt
                assert t <= l
            seen[sr] = (t, top)
            break
    t += 1
    if t == 2022:
        print(top)
print(top + added)
