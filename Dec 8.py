from sys import argv
visible = 0
max_dist = 0
file = open(argv[1] if len(argv)>1 else "treeheights.txt").read().strip()
lines = [l for l in file.split("\n")]
Dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for Y in range(len(lines)):
    for X in range(len(lines[0])):
        vis = False
        score = 1
        for (x, y) in Dir:
            dx = X
            dy = Y
            dist = 1
            br = True
            while True:
                dx += x
                dy += y
                if not (0 <= dx < len(lines[Y]) and 0 <= dy < len(lines)):
                    dist -= 1
                    break
                if int(lines[Y][X]) <= int(lines[dy][dx]):
                    br = False
                    break
                dist += 1
            score *= dist
            if br:
                vis = True
        if vis:
            visible += 1
        max_dist = max(max_dist, score)
print("P1:",visible)
print("P2:",max_dist)
