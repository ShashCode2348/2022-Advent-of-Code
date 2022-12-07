positions = [[' ',' ',' ',' ',' ',' ',' ',' ',' ']]
values = []
with open("crates.txt") as file:
    for s, line in enumerate(file):
        line = line.rstrip("\n")
        positions.append([line[i+1:i+2] for i in range(0, len(line), 4)])
        if s == 7:
            break
    for c in range(len(positions)):
        n = []
        for r in range(len(positions[c])):
            if positions[r][c] == ' ':
                continue
            n.append(positions[r][c])
        values.append(n)
    print(values)
    for s, line in enumerate(file):
        if  s < 2:
            continue
        line = line.rstrip("\n")
        instr = list(map(int, [line.split(" ")[1], line.split(" ")[3], line.split(" ")[5]]))
        for m in range(instr[0]):
            obj = values[instr[1]-1][0]
            values[instr[2]-1].insert(0, obj)
            values[instr[1]-1].remove(obj)
for col in values:
    print(col[0], end='')
