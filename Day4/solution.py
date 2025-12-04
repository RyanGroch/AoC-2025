import sys

rows = []
total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        rows.append(list(line.strip()))

    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] != '@':
                continue

            adj_count = 0

            for y in range(r - 1, r + 2):
                for x in range(c - 1, c + 2):
                    if x < 0 or y < 0 or \
                       x >= len(rows[r]) or \
                       y >= len(rows) or \
                       (y == r and x == c):
                        continue

                    if rows[y][x] == '@':
                        adj_count += 1 

            if adj_count < 4:
                total += 1

print(total)
