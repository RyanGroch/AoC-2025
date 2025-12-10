import sys

data = []
total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.split(" ")
        curr_data = {
            "lights": 0,
            "req": 0,
            "btns": []
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

print(total)
