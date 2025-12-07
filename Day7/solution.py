import sys

strands = set()
splits = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        next_strands = strands.copy()
        for i,char in enumerate(line):
            if char == 'S':
                next_strands.add(i)
            elif char == '^' and i in strands:
                splits += 1
                if i - 1 >= 0:
                    next_strands.add(i - 1)

                next_strands.add(i + 1)
                next_strands.remove(i)

        strands = next_strands

print(splits)
        