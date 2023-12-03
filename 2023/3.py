from collections import defaultdict
import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)


# reading lines
f = open(sys.argv[1], "r")
lines = [l.strip() for l in f.read().split("\n")]
lines = lines[:-1]
f.close()


# create a mapping between each number and it's coordinate
mapping = defaultdict(str)
for odx, line in enumerate(lines):
  idx = 0
  while idx < len(line):
    char = line[idx]
    if char.isdigit():
      num = ""
      track = []
      while idx < len(line) and line[idx].isdigit():
        num += line[idx]
        track.append(f"{str(odx)}_{str(idx)}")
        idx += 1
      for t in track:
        mapping[t] = num
    idx += 1


p1 = 0
p2 = 0
# go over each symbol, and if a number matches, 'visit' it's mapped number
for odx, line in enumerate(lines):
  for idx, char in enumerate(line):
    # check a symbol
    if char != "." and not char.isdigit():
      values = []
      for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
          obj = lines[odx + x][idx + y]
          if obj.isdigit():
            position = f"{odx + x}_{idx + y}"
            num = mapping[position]
            # for part 1
            if int(num) not in values:
              values.append(int(num))
              p1 += int(num)
      # check * gear, for part 2
      if char == "*" and len(values) == 2:
        p2 += values[0] * values[1]

print(f"P1: {p1}")
print(f"P2: {p2}")
