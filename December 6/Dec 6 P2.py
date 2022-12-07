with open("buffer.txt") as file:
    for line in file:
        line.rstrip("\n")
        for char in range(len(line) - 3):
            buf = []
            for n in range(14):
                buf.append(line[char+n])
            if len(set(buf)) == len(buf):
                print(char+14)
                break
