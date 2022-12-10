with open("Cathode Ray Tube.txt") as file:
    loop = 0
    X = 1
    strength = 0
    row = ""
    display = []
    for line in file:    
        instr = line.rstrip("\n").split()
        if instr[0] == "noop":
            loop += 1
            row += "#" if len(row) in range(X-1, X+2) else "."
            if len(row) == 40:
                display.append(row)
                row = ""
            if loop in {20, 60, 100, 140, 180, 220}:
                strength += loop*X
        if instr[0] == "addx":
            for _ in range(2):
                loop += 1
                if loop in {20, 60, 100, 140, 180, 220}:
                    strength += loop*X
                row += "#" if len(row) in range(X-1, X+2) else "."
                if len(row) == 40:
                    display.append(row)
                    row = ""
            X += int(instr[1])
    print("P1:", strength)
    print("P2:\n" + "\n".join(display))
            
