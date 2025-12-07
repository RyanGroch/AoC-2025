import sys

strands = set()
strands_dict = {}
splits = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()
        next_strands = strands.copy()
        next_strands_dict = strands_dict.copy()
        for i,char in enumerate(line):
            if char == 'S':
                next_strands.add(i)
                next_strands_dict[i] = 1

            elif char == '^' and i in strands:
                splits += 1

                if i - 1 >= 0:
                    next_strands.add(i - 1)
                    if i - 1 not in next_strands_dict:
                        next_strands_dict[i - 1] = strands_dict[i]
                    else:
                        next_strands_dict[i - 1] += strands_dict[i]

                if i + 1 not in next_strands_dict:
                    next_strands_dict[i + 1] = strands_dict[i]
                else:
                    next_strands_dict[i + 1] += strands_dict[i]

                del next_strands_dict[i]
                
                next_strands.add(i + 1)
                next_strands.remove(i)

        strands = next_strands
        strands_dict = next_strands_dict

print(f"Part 1: {splits}")
print(f"Part 2: {sum(strands_dict.values())}")
