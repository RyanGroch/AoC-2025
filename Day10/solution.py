import sys
from scipy.optimize import linprog

data = []
total = 0
total2 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split(" ")
        curr_data = {
            "lights": 0,
            "req": 0,
            "btns": [],
            "btns_raw": []
        }

        lights = line[0][1:len(line[0])-1]
        curr_data["lights"] = len(lights)
        for i in range(curr_data["lights"]-1, -1, -1):
            curr_data["req"] <<= 1
            if lights[i] == "#":
                curr_data["req"] |= 1

            
        for i in range(1, len(line) - 1):
            btn = line[i]
            btn_mapping = 0
            for val in btn[1:len(btn)-1].split(","):
                btn_mapping |= (1 << int(val))

            curr_data["btns"].append(btn_mapping)
            curr_data["btns_raw"].append(list(map(int, btn[1:len(btn)-1].split(","))))

        jolt_reqs = line[-1].strip()
        jolt_reqs = jolt_reqs[1:len(jolt_reqs)-1]
        curr_data["jolt_req"] = list(map(int, jolt_reqs.split(",")))

        data.append(curr_data)

min_count = float("inf")


def dfs(btns, btns_state, req, count, i):
    global min_count

    if btns_state == req:
        min_count = min(min_count, count)
        return
    
    if i >= len(btns):
        return
    
    dfs(btns, btns_state ^ btns[i], req, count+1, i+1)
    dfs(btns, btns_state, req, count, i+1)


for machine in data:
    min_count = float("inf")
    dfs(machine["btns"], 0, machine["req"], 0, 0)
    total += min_count

for machine in data:
    total2 += linprog(
        [1 for _ in machine["btns"]], 
        A_eq=[[i in b for b in machine["btns_raw"]] for i in range(len(machine["jolt_req"]))], 
        b_eq=machine["jolt_req"], 
    integrality=1).fun

print(f"Part 1: {total}")
print(f"Part 2: {int(total2)}")
