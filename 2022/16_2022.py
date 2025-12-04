import re
from collections import defaultdict

graph = {}
rates = {}
for line in open("data/16_2022.txt").read().strip().split("\n"):
    front, back = re.split(r"; tunnels? leads? to valves? ", line)
    x = front.split(" ")[1]
    rates[x] = int(front.split("=")[-1])
    graph[x] = back.split(", ")

node_id = defaultdict(lambda: len(node_id))
[node_id[u] for u in rates if rates[u]]
all_mask = (1 << len(node_id)) - 1
cache = defaultdict(lambda: [[-1 for mask in range(all_mask + 1)] for t in range(31)])


def dp(u, t, mask):
    if t == 0:
        return 0
    if cache[u][t][mask] == -1:
        best = max(dp(v, t - 1, mask) for v in graph[u])
        bit = 1 << node_id[u]
        if bit & mask:
            best = max(best, dp(u, t - 1, mask - bit) + rates[u] * (t - 1))
        cache[u][t][mask] = best
    return cache[u][t][mask]


print(dp("AA", 30, all_mask))
print(
    max(
        dp("AA", 26, all_mask - mask) + dp("AA", 26, mask)
        for mask in range(all_mask + 1)
    )
)
