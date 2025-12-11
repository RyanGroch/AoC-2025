import sys
from collections import deque

adj = {}
q = deque()

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split(":")
        adj[line[0]] = line[1].strip().split(" ")

q.append("you")
paths1 = 0

while len(q) > 0:
    loc = q.popleft()
    for dest in adj[loc]:
        if dest == "out":
            paths1 += 1
        else:
            q.append(dest)

paths2 = 0
routes = {
    ("svr", "dac"): 0, 
    ("svr", "fft"): 0, 
    ("dac", "fft"): 0,
    ("fft", "dac"): 0,
    ("dac", "out"): 0,
    ("fft", "out"): 0
}

queued = {}

for start,end in routes.keys():
    q.append(start)
    queued[start] = 1
    while len(q) > 0:
        loc = q.popleft()
        paths_to_loc = queued[loc]
        del queued[loc]

        for dest in adj[loc]:
            if dest == end:
                routes[(start,end)] += paths_to_loc
            elif dest not in ("dac", "fft", "out"):
                if dest in queued:
                    queued[dest] += paths_to_loc
                else:
                    q.append(dest)
                    queued[dest] = paths_to_loc

paths2 = \
    (routes[("svr", "dac")] * routes[("dac", "fft")] * routes[("fft", "out")]) + \
    (routes[("svr", "fft")] * routes[("fft", "dac")] * routes[("dac", "out")])

print(f"Part 1: {paths1}")
print(f"Part 2: {paths2}")
