import sys

ids = []
building_set = True
fresh1 = 0
fresh2 = 0

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
                    fresh1 += 1
                    cont = False
                    break

                if not cont:
                    break


new_ids = []
ids.sort()

for i in range(len(ids)):
    l,h = ids[i]
    if len(new_ids) > 0:
        lp,hp = new_ids[-1]
        if lp <= l <= hp or lp <= h <= hp or l <= lp <= h or l <= hp <= h:
            new_ids[-1] = (min(l, lp), max(h,hp))
        else:
            new_ids.append((l, h))
    else:
        new_ids.append((l, h))

for l,h in new_ids:
    fresh2 += (h - l + 1)

print(fresh1)
print(fresh2)
