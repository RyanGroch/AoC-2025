import sys

total_2 = 0
total_12 = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        line = line.strip()

        included = set()
        number = ["" for _ in line]
        num_chars = 0

        while num_chars < 12:
            if num_chars == 2:
                total_2 += int("".join(number))

            highest_i = 0
            highest_num = int(line[0])
            
            for i in range(1, len(line)):
                if i in included:
                    continue

                number[i] = line[i]
                curr_num = int("".join(number))
                number[i] = ""

                if curr_num > highest_num:
                    highest_i = i
                    highest_num = curr_num

            included.add(highest_i)
            number[highest_i] = line[highest_i]
            num_chars += 1

        total_12 += int("".join(number))

print(f"Part 1: {total_2}")
print(f"Part 2: {total_12}")
