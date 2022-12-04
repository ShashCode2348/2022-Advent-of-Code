max_cal1 = 0
max_cal2 = 0
max_cal3 = 0
curr_cal = 0
with open("cal.txt") as file:
    for line in file:
        if line == "\n":
            if curr_cal > max_cal1:
                max_cal3 = max_cal2
                max_cal2 = max_cal1
                max_cal1 = curr_cal
            elif curr_cal > max_cal2:
                max_cal3 = max_cal2
                max_cal2 = curr_cal
            elif curr_cal > max_cal3:
                max_cal3 = curr_cal
            curr_cal = 0
            continue
        line = line.rstrip("\n")
        curr_cal += int(line)
print(max_cal1+max_cal2+max_cal3)
