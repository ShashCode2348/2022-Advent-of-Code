prioritySum = 0
types = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open("rucksacks.txt") as file:
    for line in file:
        line = line.rstrip("\n")
        str1 = line[0:int(len(line)/2)]
        str2 = line[int(len(line)/2):len(line)]
        for char in str1:
            if char in str2:
                prioritySum += types.find(char) + 1
                break
print(prioritySum)
