import sys
from collections import Counter, defaultdict

inf = sys.argv[1] if len(sys.argv) > 1 else "day21data.txt"

ll = [int(x.split(": ")[1]) for x in open(inf).read().strip().split("\n")]

dice = 1
score = [0, 0]
done = False
while not done:
    for player in range(2):
        newpos = (ll[player] + dice + dice + 1 + dice + 2 - 1) % 10 + 1
        dice += 3
        score[player] += newpos
        ll[player] = newpos
        if score[player] >= 1000:
            print(score[1 - player] * (dice - 1))
            done = True
            break

ll = [int(x.split(": ")[1]) for x in open(inf).read().strip().split("\n")]

dice = list(
    Counter(i + j + k for i in (1, 2, 3) for j in (1, 2, 3) for k in (1, 2, 3)).items()
)

universes = {((0, ll[0]), (0, ll[1]), 0): 1}
wins = [0, 0]
while universes:
    cpy = list(universes.items())
    universes = defaultdict(int)
    for state, cnt in cpy:
        turn = state[2]
        score, pos = state[turn]
        state = list(state)
        state[2] = 1 - turn
        for roll, dcount in dice:
            newpos = (pos + roll - 1) % 10 + 1
            newscore = score + newpos
            if newscore >= 21:
                wins[turn] += cnt * dcount
                continue
            state[turn] = (newscore, newpos)
            universes[tuple(state)] += cnt * dcount
print(max(wins))
