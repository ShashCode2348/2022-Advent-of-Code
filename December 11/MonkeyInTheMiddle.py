from sys import argv
from copy import deepcopy
lines = open(argv[1] if len(argv)>1 else "MonkeyInTheMiddle.txt").read().strip().split("\n")
monkeyInfo = []
monkeyItems = []
def operation(old, op):
    try:
        n = int(op[2:])
    except ValueError:
        n = old
    if op[0] == "+":
        return old+n
    if op[0] == "*":
        return old*n
for l, line in enumerate(lines):
    if l % 7 == 1:
        newLine = line[18:]
        monkeyItems.append(list(map(int, newLine.split(", "))))
    if l % 7 == 2:
        inf = [line[23:]]
    if l % 7 == 3:
        inf.append(int(line[21:]))
    if l % 7 == 4 or l % 7 == 5:
        inf.append(int(line.split()[5]))
    if l % 7 == 5:
        monkeyInfo.append(inf)
lcm = 1
monkeyItemsO = deepcopy(monkeyItems)
for i in monkeyInfo:
    lcm *= i[1]
for p in [1, 2]:
    processed = [0 for _ in range(len(monkeyInfo))]
    monkeyItems = deepcopy(monkeyItemsO)
    for _ in range(20 if p==1 else 10000):
        for m in range(len(monkeyItems)):
            for item in monkeyItems[m]:
                processed[m] += 1
                item = operation(item, monkeyInfo[m][0])
                if p == 2:
                    item %= lcm
                if p == 1:
                    item = item//3
                if item % monkeyInfo[m][1] == 0:
                    monkeyItems[monkeyInfo[m][2]].append(item)
                else:
                    monkeyItems[monkeyInfo[m][3]].append(item)
            monkeyItems[m] = []
    print(sorted(processed)[-1] * sorted(processed)[-2])
        
