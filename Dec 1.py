max_cal = 0
curr_cal = 0
with open("cal.txt") as file:
    for line in file:
        if line == "\n":
            if curr_cal > max_cal:
                max_cal = curr_cal
            curr_cal = 0
            continue
        line = line.rstrip("\n")
        curr_cal += int(line)
print(max_cal)
