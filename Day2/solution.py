from pathlib import Path
import sys

input = Path(sys.argv[1]).read_text()
ranges = input.split(",")

part1_total = 0

for r in ranges:
    # print(ranges[3])
    low,high = r.split("-")
    for id in range(int(low), int(high) + 1):
        id_str = str(id)
        valid = True

        if len(id_str) == 1:
            continue

        for i in range(1, len(id_str)):
            if len(id_str) % i != 0:
                continue

            pattern = id_str[:i]

            if 2*len(pattern) != len(id_str):
                continue

            repeats = True
            for j in range(i, len(id_str), len(pattern)):
                subsection = id_str[j:j+len(pattern)]
                # print(id_str, pattern, subsection, j)
                if subsection != pattern:
                    repeats = False
                    break
            
            if repeats:
                valid = False
                part1_total += id
                print(id_str, pattern)
                break

    # print(r)

print(part1_total)
