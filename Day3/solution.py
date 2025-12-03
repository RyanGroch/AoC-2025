import sys

total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        curr_max = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                current_pair = str(line[i]) + str(line[j])
                curr_max = max(curr_max, int(current_pair))

        total += curr_max

print(total)
