import sys

rows = []
removed = -1
total_1 = 0
total_2 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        rows.append(list(line.strip()))

while removed != 0:
    removed = 0
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
                       (y == r and x == c) or \
                       rows[y][x] != '@':
                        continue

                    adj_count += 1 

            if adj_count < 4:
                removed += 1
                if total_1 != 0:
                    rows[r][c] = "."

    if total_1 == 0:
        total_1 = removed
    else:
        total_2 += removed

print(f"Part 1: {total_1}")
print(f"Part 2: {total_2}")
