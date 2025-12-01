import sys

rotations = []

with open(sys.argv[1], "r") as f:
    for line in f:
        rotations.append(line)


def part1():
    pos = 50
    password = 0

    for rot in rotations:
        direction = rot[0]
        amount = int(rot[1:])

        if direction == "R":
            pos += amount
        else:
            pos -= amount

        while pos < 0:
            pos += 100

        pos %= 100

        if pos == 0:
            password += 1
    
    return password


def part2():
    pos = 50
    password = 0

    for rot in rotations:
        direction = rot[0]
        amount = int(rot[1:])
        start_0 = pos == 0

        if direction == "R":
            pos += amount
        else:
            pos -= amount

        if pos == 0:
            password += 1

        while pos < 0:
            pos += 100

            if not start_0:
                password += 1
            else:
                start_0 = False

            if pos == 0:
                password += 1

        while pos > 99:
            pos -= 100
            password += 1

    return password

print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")
