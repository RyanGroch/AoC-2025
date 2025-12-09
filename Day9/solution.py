import sys
import math

tiles = []
max_area = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip().split(",")
        tiles.append((int(line[0]), int(line[1])))

for i,tile1 in enumerate(tiles):
    for j in range(i, len(tiles)):
        tile2 = tiles[j]

        area = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        max_area = max(max_area, area)

print(max_area)
