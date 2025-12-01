import sys

pos = 50
count = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        direction = line[0]
        amount = int(line[1:])

        if direction == "R":
            pos += amount
        else:
            pos -= amount

        while pos < 0:
            pos += 100

        pos %= 100

        if pos == 0:
            count += 1

print(count)
