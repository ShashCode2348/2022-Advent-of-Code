rangeContained = 0
with open("pairs.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        p1, p2 = line.split(',')
        rP1 = list(range(int(p1.split("-")[0]), int(p1.split("-")[1])+1))
        rP2 = list(range(int(p2.split("-")[0]), int(p2.split("-")[1])+1))
        if all([item in rP1 for item in rP2]):
            rangeContained += 1
        elif all([item in rP2 for item in rP1]):
            rangeContained += 1
print(rangeContained)

