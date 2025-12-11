import sys
from collections import deque

adj = {}
q = deque()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split(":")
        adj[line[0]] = line[1].strip().split(" ")

# seen.add("you")
q.append("you")
paths = 0

while len(q) > 0:
    loc = q.popleft()
    for dest in adj[loc]:
        if dest == "out":
            paths += 1
        else:
            q.append(dest)

print(paths)
