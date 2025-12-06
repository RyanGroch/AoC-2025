import sys

problems = []
total = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        i = 0
        items = line.split(" ")
        for item in items:
            item = item.strip()
            if not item:
                continue

            if i >= len(problems):
                problems.append([item])
            else:
                problems[i].append(item)

            i += 1

# print(problems)

for prob in problems:
    addition = prob[-1] == '+'
    curr_total = 0

    if addition:
        for j in range(4):
            curr_total += int(prob[j])
    else:
        curr_total = 1
        for j in range(4):
            curr_total *= int(prob[j])

    total += curr_total
    # print(curr_total)

print(total)
