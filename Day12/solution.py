import sys

patterns = [[] for _ in range(6)]
problems = []

with open(sys.argv[1], "r") as f:
    pat_count = 0
    lines_in_pat = 0
    for line in f:
        line = line.strip()

        if pat_count <= 5:
            if lines_in_pat >= 3:
                lines_in_pat = 0
                pat_count += 1

            if not line or line[0] not in ("#", "."):
                continue

            patterns[pat_count].append(list(line))
            lines_in_pat += 1

        else:
            dims,counters = line.split(":")
            x,y = dims.split("x")
            parsed_counters = list(map(int, counters.strip().split(" ")))
            problems.append(((int(x), int(y)), parsed_counters))

pattern_sz = [
    sum(
        (sum([char == "#" for char in row]) for row in pat)
    ) for pat in patterns
]

total = 0

for dims,counters in problems:
    space_req = sum(pattern_sz[i]*counters[i] for i in range(len(counters)))
    total_space = dims[0]*dims[1]
    if space_req < total_space:
        total += 1

print(total)
