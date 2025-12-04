import sys
import heapq

sys.setrecursionlimit(int(1e6))
data = sys.argv[1] if len(sys.argv) > 1 else "day15data.txt"
G = []
for line in open(data):
    G.append([int(x) for x in line.strip()])
R = len(G)
C = len(G[0])
DR = [-1, 0, 1, 0]
DC = [0, 1, 0, -1]


def solve(nTiles):
    D = [[None for _ in range(nTiles * C)] for _ in range(nTiles * R)]
    Q = [(0, 0, 0)]
    while Q:
        (dist, r, c) = heapq.heappop(Q)
        if r < 0 or r >= nTiles * R or c < 0 or c >= nTiles * C:
            continue
        val = G[r % R][c % C] + (r // R) + (c // C)
        while val > 9:
            val -= 9
        rcCost = dist + val
        if D[r][c] is None or rcCost < D[r][c]:
            D[r][c] = rcCost
        else:
            continue
        if r == nTiles * R - 1 and c == nTiles * C - 1:
            break
        for d in range(4):
            rr = r + DR[d]
            cc = c + DC[d]
            heapq.heappush(Q, (D[r][c], rr, cc))
    return D[nTiles * R - 1][nTiles * C - 1] - G[0][0]


print(solve(1))
print(solve(5))
