import re
import heapq

input = "data/21_2024.txt"
data = open(input).read().strip()
pad1 = ["789", "456", "123", " 0A"]
pad2 = [" ^A", "<v>"]
dp = {}


def ints(s):
    return [int(x) for x in re.findall("-?\d+", s)]


def get_pad1(p1):
    r, c = p1
    if not (0 <= r < len(pad1) and 0 <= c < len(pad1[r])):
        return None
    if pad1[r][c] == " ":
        return None
    return pad1[r][c]


def get_pad2(p):
    r, c = p
    if not (0 <= r < len(pad2) and 0 <= c < len(pad2[r])):
        return None
    if pad2[r][c] == " ":
        return None
    return pad2[r][c]


def apply_pad1(p, move):
    if move == "A":
        return (p, get_pad1(p))
    elif move == "<":
        return ((p[0], p[1] - 1), None)
    elif move == "^":
        return ((p[0] - 1, p[1]), None)
    elif move == ">":
        return ((p[0], p[1] + 1), None)
    elif move == "v":
        return ((p[0] + 1, p[1]), None)


def apply_pad2(p, move):
    if move == "A":
        return (p, get_pad2(p))
    elif move == "<":
        return ((p[0], p[1] - 1), None)
    elif move == "^":
        return ((p[0] - 1, p[1]), None)
    elif move == ">":
        return ((p[0], p[1] + 1), None)
    elif move == "v":
        return ((p[0] + 1, p[1]), None)


def solve(code, pads):
    start = [0, (3, 2), "A", "", ""]
    q, vis = [], {}
    heapq.heappush(q, start)
    while q:
        d, p1, p2, out, path = heapq.heappop(q)
        assert p2 in ["<", ">", "v", "^", "A"]
        if out == code:
            return d
        if not code.startswith(out):
            continue
        if get_pad1(p1) is None:
            continue
        key = (p1, p2, out)
        if key in vis:
            assert d >= vis[key], f"{key=} {d=} {vis[key]=}"
            continue
        vis[key] = d
        for move in ["^", "<", "v", ">", "A"]:
            new_p1 = p1
            new_out = out
            new_p1, output = apply_pad1(p1, move)
            if output is not None:
                new_out = out + output
            cost_move = cost(move, p2, pads)
            new_path = path
            assert cost_move >= 0
            heapq.heappush(q, [d + cost_move, new_p1, move, new_out, new_path])


def cost(ch, prev_move, pads):
    key = (ch, prev_move, pads)
    if key in dp:
        return dp[key]
    if pads == 0:
        return 1
    else:
        assert ch in ["^", ">", "v", "<", "A"]
        assert prev_move in ["^", ">", "v", "<", "A"]
        assert pads >= 1
        q = []
        start_pos = {"^": (0, 1), "<": (1, 0), "v": (1, 1), ">": (1, 2), "A": (0, 2)}[
            prev_move
        ]
        heapq.heappush(q, [0, start_pos, "A", "", ""])
        vis = {}
        while q:
            d, p, prev, out, path = heapq.heappop(q)
            if get_pad2(p) is None:
                continue
            if out == ch:
                dp[key] = d
                return d
            elif len(out) > 0:
                continue
            vis_key = (p, prev)
            if vis_key in vis:
                assert d >= vis[vis_key]
                continue
            vis[vis_key] = d
            for move in ["^", "<", "v", ">", "A"]:
                new_p, output = apply_pad2(p, move)
                cost_move = cost(move, prev, pads - 1)
                new_d = d + cost_move
                new_path = path
                new_out = out
                if output is not None:
                    new_out = new_out + output
                heapq.heappush(q, [new_d, new_p, move, new_out, new_path])
        assert False, f"{ch=} {pads=}"


p1 = 0
p2 = 0
for line in data.split("\n"):
    s1 = solve(line, 2)
    s2 = solve(line, 25)
    line_int = ints(line)[0]
    p1 += line_int * s1
    p2 += line_int * s2
print(p1)
print(p2)
