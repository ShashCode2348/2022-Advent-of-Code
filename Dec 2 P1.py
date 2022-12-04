score = 0
with open("strategy.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        if line == "A X":
            score += 4
        elif line == "A Y":
            score += 8
        elif line == "A Z":
            score += 3
        elif line == "B X":
            score += 1
        elif line == "B Y":
            score += 5
        elif line == "B Z":
            score += 9
        elif line == "C X":
            score += 7
        elif line == "C Y":
            score += 2
        elif line == "C Z":
            score += 6
print(score)
