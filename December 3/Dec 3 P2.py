prioritySum = 0
n = 0
types = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("rucksacks.txt") as file:
    for i, line in enumerate(file):
        if i % 3 == 0:
            ln1 = line.rstrip("\n")
        elif i % 3 == 1:
            ln2 = line.rstrip("\n")
        elif i % 3 == 2:
            ln3 = line.rstrip("\n")
            for char in ln1:
                if char in ln2 and char in ln3:
                    prioritySum += types.find(char) + 1
                    break
print(prioritySum)
