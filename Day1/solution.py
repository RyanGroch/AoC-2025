import sys

pos = 50
password1 = 0
password2 = 0

with open(sys.argv[1], "r") as f:
    for rot in f:
        direction = rot[0]
        amount = int(rot[1:])
        start_0 = pos == 0

        if direction == "R":
            pos += amount
        else:
            pos -= amount

        if pos == 0:
            password2 += 1

        while pos < 0:
            pos += 100

            if not start_0:
                password2 += 1
            else:
                start_0 = False

            if pos == 0:
                password2 += 1

        while pos > 99:
            pos -= 100
            password2 += 1

        if pos == 0:
            password1 += 1

print(f"Part 1: {password1}")
print(f"Part 2: {password2}")
