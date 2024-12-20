infile = "data/19_2024.txt"
data = open(infile).read().strip()
words, targets = data.split("\n\n")
words = words.split(", ")
p1, p2, dp = 0, 0, {}


def ways(words, target):
    if target in dp:
        return dp[target]
    ans = 0
    if not target:
        ans = 1
    for word in words:
        if target.startswith(word):
            ans += ways(words, target[len(word) :])
    dp[target] = ans
    return ans


for target in targets.split("\n"):
    target_ways = ways(words, target)
    if target_ways > 0:
        p1 += 1
    p2 += target_ways


print(p1)
print(p2)
