import sys
import math

points = []
connections = []
circuits_table = {}
circuits_rev = {}

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        x,y,z = line.split(",")
        points.append((int(x), int(y), int(z)))

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        dist = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
        connections.append((dist, p1, p2))

connections.sort(key = lambda x: x[0])

def connect(i):
    conn = connections[i]

    if conn[1] in circuits_table and conn[2] in circuits_table:
        s1 = circuits_table[conn[1]]
        s2 = circuits_table[conn[2]]

        if s1 is s2:
            return

        s3 = s1.union(s2)

        l1 = circuits_rev[id(s1)]
        l2 = circuits_rev[id(s2)]

        l3 = l1 + l2

        for point in l3:
            circuits_table[point] = s3

        del circuits_rev[id(s1)]
        del circuits_rev[id(s2)]

        circuits_rev[id(s3)] = l3

    elif conn[1] in circuits_table:
        s = circuits_table[conn[1]]
        s.add(conn[2])
        circuits_table[conn[2]] = s
        circuits_rev[id(s)].append(conn[2])

    elif conn[2] in circuits_table:
        s = circuits_table[conn[2]]
        s.add(conn[1])
        circuits_table[conn[1]] = s
        circuits_rev[id(s)].append(conn[1])

    else:
        s = set()
        s.add(conn[1])
        circuits_table[conn[1]] = s
        s.add(conn[2])
        circuits_table[conn[2]] = s
        circuits_rev[id(s)] = [conn[1], conn[2]]


for i in range(1000):
    connect(i)

final = list(circuits_rev.values())
final.sort(key=lambda x: len(x), reverse=True)
total = len(final[0]) * len(final[1]) * len(final[2])

i = 1000
while i < len(connections):
    connect(i)

    if len(circuits_rev) == 1 and len(circuits_table) == 1000:
        break

    i += 1

print(f"Part 1: {total}")
print(f"Part 2: {connections[i][1][0] * connections[i][2][0]}")
