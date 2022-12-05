import sys
from math import ceil


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)

f = open("5.in", "r")
lines = f.read().splitlines()

# todo: pick from file, don't be naughty
columns = [[], [], [], [], [], [], [], [], []]

# which part
p1, p2 = False, False
if sys.argv[1] == "1":
    p1 = True
else:
    p2 = True

for line in lines:
    # read alphabet
    if "[" in line:
        for i, v in enumerate(line):
            if 65 <= ord(v) <= 90:
                columns[(i - 1) // 4].append(v)

    # have read columns, reverse their order
    if line == "":
        for col in columns:
            col.reverse()

    # move command
    if "move" in line:
        # todo: this can be way better through regex
        what = int(line.split(" from")[0].split("move ")[1])
        fromC = int(line.split("from ")[1].split(" to")[0])
        to = int(line.split("to ")[1])

        if p1:
            # move crates
            for _ in range(what):
                v = columns[fromC - 1].pop()
                columns[to - 1].append(v)

        if p2:
            # store which crates to move
            temp = []
            for _ in range(what):
                v = columns[fromC - 1].pop()
                temp.append(v)

            # move crates in order
            temp.reverse()
            for v in temp:
                columns[to - 1].append(v)

# answer
output = ""
for col in columns:
    output += col.pop()
print(output)
