import sys

problems = []
chars = []
intermed = []
problems_2 = []
total = 0
total_2 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        i = 0

        chars.append(list(line))
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

prev_break_point = 0
break_point = 0

for k in range(len(chars[0])):
    if chars[0][k] == chars[1][k] == chars[2][k] == chars[3][k] == " ":
        prev_break_point = break_point
        break_point = k

        intermed.append([
            chars[0][prev_break_point:break_point],
            chars[1][prev_break_point:break_point],
            chars[2][prev_break_point:break_point],
            chars[3][prev_break_point:break_point]
        ])

intermed.append([
    chars[0][break_point:],
    chars[1][break_point:],
    chars[2][break_point:],
    chars[3][break_point:]
])

for p in range(len(intermed)):
    curr = []
    for d in range(len(intermed[p][0])):
        curr.append(int("".join([
                    intermed[p][0][d],
                    intermed[p][1][d],
                    intermed[p][2][d],
                    intermed[p][3][d],
                ]).strip() or 0
            )
        )
        curr = list(filter(lambda x: x != 0, curr))

    problems_2.append(curr)

for prob in problems:
    addition = prob[-1] == '+'
    curr_total = 0
    curr_total_2 = 0

    if addition:
        for j in range(4):
            curr_total += int(prob[j])
    else:
        curr_total = 1
        for j in range(4):
            curr_total *= int(prob[j])

    total += curr_total

for q in range(len(problems_2)):
    addition = problems[q][-1] == '+'
    prob = problems_2[q]
    curr_total_2 = 0

    if addition:
        for j in range(len(prob)):
            curr_total_2 += int(prob[j])
    else:
        curr_total_2 = 1
        for j in range(len(prob)):
            curr_total_2 *= int(prob[j])

    total_2 += curr_total_2

print(total)
print(total_2)
