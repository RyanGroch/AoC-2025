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


for i in range(len(ids)):
    low,high = ids[i]
    low = int(low)
    high = int(high)
    extra_pass = True

    while extra_pass:
        extra_pass = False
        for j in range(i):
            prev_low,prev_high = ids[j]
            prev_low = int(prev_low)
            prev_high = int(prev_high)

            if low >= prev_low and low <= prev_high:
                extra_pass = True
                low = prev_high + 1

            if high >= prev_low and high <= prev_high:
                extra_pass = True
                high = prev_low - 1

    if low <= high:
        # print("IGNORED: ", ids[i], low, high)
        fresh2 += (1 + high - low)
        continue

    # print(ids[i], low,high, (high - low + 1))

print(fresh1)
print(fresh2)
