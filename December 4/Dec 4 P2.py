overlap = 0
with open("pairs.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        p1, p2 = line.split(',')
        rP1 = list(range(int(p1.split("-")[0]), int(p1.split("-")[1])+1))
        rP2 = list(range(int(p2.split("-")[0]), int(p2.split("-")[1])+1))
        for item in rP1:
            if item in rP2:
                overlap += 1
                break
print(overlap)
