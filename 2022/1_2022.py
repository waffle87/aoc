i = [l.strip() for l in open("day1data.txt")]
j = []
for elf in ("\n".join(i)).split("\n\n"):
    k = 0
    for x in elf.split("\n"):
        k += int(x)
    j.append(k)
j = sorted(j)
print(j[-1])
print(j[-1] + j[-2] + j[-3])
