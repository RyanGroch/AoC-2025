import sys

pos = 50
count = 0

with open(sys.argv[1], "r") as f:
    for line in f:
        direction = line[0]
        amount = int(line[1:])
        start_0 = pos == 0

        if direction == "R":
            pos += amount
        else:
            pos -= amount

        if pos == 0:
            count += 1

        while pos < 0:
            pos += 100

            if not start_0:
                count += 1
            else:
                start_0 = False

            if pos == 0:
                count += 1

        while pos > 99:
            pos -= 100
            count += 1

print(count)
