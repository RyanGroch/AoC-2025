import sys

ids = []
building_set = True
fresh = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        if building_set:
            if line == "":
                building_set = False
                continue

            low,high = line.split("-")
            ids.append((int(low), int(high)))
        else:
            check = int(line)
            for low, high in ids:
                cont = True
                if check >= low and check <= high:
                    fresh += 1
                    cont = False
                    break

                if not cont:
                    break

print(fresh)
