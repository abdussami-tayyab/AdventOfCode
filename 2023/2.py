import sys


if len(sys.argv) == 1:
  print("ERROR: Enter part # as argument")
  sys.exit(0)

# reading lines
f = open(sys.argv[1], "r")
lines = [l.strip() for l in f.read().split("\n")]
lines = lines[:-1]
f.close()

# vars
BLUE_LIMIT = 14
GREEN_LIMIT = 13
RED_LIMIT = 12
BLUE = 0
GREEN = 0
RED = 0
total = 0
total2 = 0
p1 = sys.argv[2] == "p1"
p2 = sys.argv[2] == "p2"

for idx, game in enumerate(lines):
  invalid = False
  colors = game.split(": ")[1]
  bags = [x.strip() for x in colors.split("; ")]

  red = -1
  blue = -1
  green = -1

  for bag in bags:
    colors = [x.strip() for x in bag.split(",")]
    for color in colors:
      num, colorval = color.split()
      num = int(num)
        
      if colorval == "blue" and ((p2 == True and num > blue) or (p1 == True and num > BLUE_LIMIT)):
        blue = num
        if p1:
          invalid = True
      elif colorval == "green" and ((p2 == True and num > green) or (p1 == True and num > GREEN_LIMIT)):
        green = num
        if p1:
          invalid = True
      elif colorval == "red" and ((p2 == True and num > red) or (p1 == True and num > RED_LIMIT)):
        red = num
        if p1:
          invalid = True
    if invalid:
      break

  total2 += (red * green * blue)

  if not invalid:
    total += idx + 1

if p1:
  print(total)
else:
  print(total2)
